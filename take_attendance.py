import cv2
import os
import numpy as np
import csv
from datetime import datetime

# Directory paths
base_dir = os.path.dirname(os.path.abspath(__file__))
faces_dir = os.path.join(base_dir, 'data/faces')
unknown_dir = os.path.join(base_dir, 'data/unknown')

# Function to load known faces and assign unique IDs
def load_known_faces():
    known_faces = []
    labels = []
    label_ids = {}  # Dictionary to map labels to numeric IDs
    current_id = 0

    for root, dirs, files in os.walk(faces_dir):
        for file in files:
            if file.endswith("jpg") or file.endswith("png"):
                img_path = os.path.join(root, file)
                label = os.path.splitext(file)[0].rsplit('_', 1)[0]  # Extract the actual name from the file name

                # Assign a unique numeric ID to each label (person)
                if label not in label_ids:
                    label_ids[label] = current_id
                    current_id += 1

                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    print(f"Warning: Image {img_path} could not be read.")
                    continue
                known_faces.append(img)
                labels.append(label_ids[label])

    return known_faces, labels, label_ids

# Recognize faces in real-time and mark attendance
def recognize_faces():
    known_faces, labels, label_ids = load_known_faces()

    if len(known_faces) == 0:
        print("No faces found in the dataset.")
        return

    # Initialize LBPH face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(known_faces, np.array(labels))

    # Initialize video capture
    video_capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    last_logged_time = {}
    logged_users_today = set()

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture image from camera.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_detected = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces_detected:
            face_roi = gray[y:y+h, x:x+w]
            face_resized = cv2.resize(face_roi, (100, 100))

            # Predict the face using the recognizer
            label_id, confidence = recognizer.predict(face_resized)

            # Match the predicted ID with the label to get the name
            predicted_name = "Unknown Person"
            for name, id_ in label_ids.items():
                if id_ == label_id:
                    predicted_name = name
                    break

            # Print debug information
            print(f"Detected {predicted_name} with confidence {confidence}")

            # Draw rectangle and display name
            if confidence < 65:  # Adjust the confidence threshold as needed
                color = (0, 255, 0)  # Green frame for recognized persons
                current_time = datetime.now()

                # Log attendance only if the user has not been logged today
                current_date = current_time.strftime("%Y-%m-%d")
                if predicted_name not in logged_users_today:
                    log_attendance(predicted_name)
                    logged_users_today.add(predicted_name)
                    last_logged_time[predicted_name] = current_time
            else:
                predicted_name = "Unknown Person"
                color = (0, 0, 255)  # Red frame for unknown persons

                # Save unknown person's photo
                if not os.path.exists(unknown_dir):
                    os.makedirs(unknown_dir)
                cv2.imwrite(os.path.join(unknown_dir, f"unknown_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"), frame)

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, predicted_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        # Display the frame with rectangles and names
        cv2.imshow('Attendance System', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

# Function to log attendance in CSV file
def log_attendance(predicted_name):
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    # Open the attendance file in append mode
    with open(current_date + '.csv', 'a', newline='') as f:
        lnwriter = csv.writer(f)
        lnwriter.writerow([predicted_name, current_time])

if __name__ == "__main__":
    recognize_faces()

