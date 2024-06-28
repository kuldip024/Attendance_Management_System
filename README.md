
## Smart Attendance System

### Description
The Smart Attendance System automates attendance using facial recognition. It creates a database, registers users by capturing 10-20 photos, and logs attendance with a timestamp. It detects unknown persons with a red frame, captures 5-10 photos, and saves them in the database for future reference.

1. **Database Creation:** Initializes a database to store registered and unknown faces.
2. **User Registration:** Registers users by capturing 10-20 photos of their faces and recording their names.
3. **Attendance Taking:** Recognizes registered users during attendance and displays a green frame with the person's name around their face, recording their attendance with the current time and date in a CSV file.
4. **Unknown Person Detection:** If an unregistered person is detected, it shows a red frame with "Unknown Person" around their face, captures 5-10 photos of the unknown person, and stores them in the database for further analysis or registration.

### File Structure

- **data/**
  - `registered_faces/` - Stores photos of registered users.
  - `unknown_faces/` - Stores photos of unidentified individuals.
- **GUI/**
  - `main.py` - Main script for the graphical user interface.
  - `styles.py` - Contains style definitions for the GUI.
- `create_database.py` - Script to set up the initial database.
- `register_user.py` - Script for user registration.
- `take_attendance.py` - Script for capturing attendance.

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/smart-attendance-system.git
   cd smart-attendance-system
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the main script:**
   ```bash
   python GUI/main.py
   ```

### Usage

- **User Registration:**
  - Use the GUI to add new users by capturing their photos and recording their names.
  
- **Taking Attendance:**
  - Use the GUI to start the attendance session. The system will automatically detect registered users and record their attendance, while capturing and storing photos of unknown individuals.

### Contributing

We welcome and appreciate contributions! Feel free to fork the repository and submit pull requests to help improve the system.

### License

This project is licensed under the MIT License. Enjoy a hassle-free, automated attendance experience with our Smart Attendance System!

