import os
import pandas as pd

def create_database():
    # Create directories and CSV
    face_dir = 'data/faces'
    csv_path = 'data/attendance.csv'

    if not os.path.exists(face_dir):
        os.makedirs(face_dir)

    if not os.path.exists(csv_path):
        df = pd.DataFrame(columns=["Name", "Date", "Time"])
        df.to_csv(csv_path, index=False)

    print("Database created successfully.")

if __name__ == "__main__":
    create_database()
