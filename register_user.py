import cv2
import os

# Directory for storing faces
faces_dir = 'data/faces'

def register_face(name):
    # Initialize video capture
    video_capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    face_count = 0

    while face_count < 20:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_detected = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces_detected:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            face_count += 1

            # Save the face region of interest
            face_roi = gray[y:y+h, x:x+w]
            face_filename = os.path.join(faces_dir, f'{name}_{face_count}.jpg')
            cv2.imwrite(face_filename, face_roi)

            # Display name near the face
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow('Register Face', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Create faces directory if it doesn't exist
    if not os.path.exists(faces_dir):
        os.makedirs(faces_dir)

    name = input("Enter the name of the person: ")
    register_face(name)