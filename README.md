# Course Registration System

A simple course registration system built using Python (console-based).

## Overview

A console-based Course Registration System developed using core Python concepts. This project simulates a real-world student registration process where users can:

- View available courses
- Register using their details
- Modify their selection
- Confirm registration
- Store data permanently using file handling

## Key Features

- Display available courses with numbered options
- Register using Registration Number and Name
- Select course using number (to avoid typing errors)
- Modify selected course before final submission
- Confirm and complete registration
- Save data permanently using file handling
- Admin panel to view and manage registered students
- Clean and formatted output display

## How to Run

### Student Registration

Run the main file:

```bash
python student_course_registration.py
```

Enter details and complete registration.

### Admin Panel

Run the admin file:

```bash
python admin_view.py
```

Choose options:
- View all students
- Search by registration number

## Project Files

| File Name | Description |
|-----------|-------------|
| `student_course_registration.py` | Main program for student registration (writes data) |
| `admin_view.py` | Admin panel to view/search records (reads data) |
| `data.txt` | Stores registered student data permanently |

## System Architecture

| Component | Role |
|-----------|------|
| `main.py` | Writes data |
| `admin.py` | Reads data |
| `data.txt` | Stores data |

## Data Storage Format

Data is stored in a simple text file (`data.txt`):

```
101,Arun,Python
102,Kumar,Maths
```

## Notes

- This project uses file handling instead of a database
- Data is stored permanently in `data.txt`
- Ensure all files are placed in the same folder

## What I Learned

- Fundamentals of Python programming
- File handling (read/write operations)
- Data storage and retrieval
- Designing real-world systems using logic
- Creating user-friendly console applications

## Author

**Siddarthan M**  
2nd Year CSE Student, Kalasalingam University

- **LinkedIn:** https://www.linkedin.com/in/siddarthan1009
- **Email:** siddarthanm2007@gmail.com