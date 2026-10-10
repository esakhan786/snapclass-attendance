# SnapClass — AI Attendance

SnapClass is a Streamlit attendance app for teachers and students. Teachers can manage subjects and record attendance using classroom photos or voice recordings. Students can register with a face profile, sign in using face recognition, enroll in subjects, and view their attendance.

## Features

- Teacher registration and login
- Subject creation and student enrollment
- Face-recognition student registration and attendance
- Optional voice enrollment and voice-based attendance
- Attendance records for teachers and attendance summaries for students
- Shareable subject links and QR codes for enrollment

## Requirements

- Python 3.10 or newer
- A Supabase project with the tables and relationships used by the app
- A camera and microphone for face and voice features

The Python dependencies are listed in [`requirements.txt`](requirements.txt). Face-recognition dependencies such as `dlib-bin` may require extra setup depending on your operating system and Python version.

## Setup

1. Clone the repository and open its directory:

   ```bash
   git clone https://github.com/<your-github-username>/snapclass-attendance.git
   cd snapclass-attendance
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the project dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Configure your Supabase credentials in `.streamlit/secrets.toml`:

   ```toml
   SUPABASE_URL = "https://your-project-id.supabase.co"
   SUPABASE_KEY = "your-supabase-key"
   ```

   Keep this file private. Do not commit real credentials to GitHub. In deployment, configure `SUPABASE_URL` and `SUPABASE_KEY` using the hosting provider's secrets settings.

5. Start the app:

   ```bash
   streamlit run app.py
   ```

## Supabase setup

The app expects a Supabase database containing these tables:

- `teachers` — teacher usernames, password hashes, and names
- `students` — student names and face/optional voice embeddings
- `subjects` — subject codes, names, sections, and teacher IDs
- `subject_students` — student-to-subject enrollments
- `attendance_logs` — student attendance by subject and timestamp

Configure the foreign-key relationships used by the app, including the subject/student relationships queried through Supabase. Passwords are hashed by the app before being stored.

## Privacy note

Student face embeddings and optional voice embeddings are stored in Supabase for recognition. Only use this system with appropriate notice, consent, and safeguards for the people whose data is collected.

## Tech stack

- Python and Streamlit
- Supabase
- dlib and scikit-learn for face recognition
- Resemblyzer and librosa for voice recognition
