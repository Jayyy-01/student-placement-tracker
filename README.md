#  Student Placement Tracker

A Python console application that manages student placement profiles, validates mock test scores, determines placement readiness, and tracks registered students — built to demonstrate core Object-Oriented Programming (OOP) concepts in Python.

---

##  Overview

The **Student Placement Tracker** allows users to:

- Add new students with unique IDs
- View all registered student profiles
- Update a student's mock test score (with validation)
- Change the shared platform name across all records
- View the total number of registered students
- Exit the application safely

This project was built as part of the **KodNest Python (OOP) curriculum**, applying concepts such as encapsulation, class/instance methods, properties, and alternative constructors in a single, self-contained script.

---

##  Features

| Feature | Description |
|---|---|
|  Add Student | Register a student with ID, name, branch, and mock score |
|  Display Students | View all stored student profiles with placement status |
|  Update Score | Modify a student's score with built-in validation (0–100) |
|  Change Platform | Update a shared "platform" value across all students |
|  Total Count | Track the number of students registered, using a class variable |

---

##  Tech Stack

- **Language:** Python 3.x
- **Paradigm:** Object-Oriented Programming (OOP)
---

##  OOP Concepts Demonstrated

- Classes & Objects
- Constructors (`__init__`) and Alternative Constructors (`@classmethod`)
- Instance Variables vs. Class Variables
- Encapsulation using Private Attributes (`__score`)
- Properties & Setters (`@property`, `@x.setter`)
- Instance Methods, Class Methods (`cls`), and Static Methods (`@staticmethod`)
- Input validation and control flow (loops, conditionals)

---

##  Project Structure

```
student-placement-tracker/
├── main.py        # Complete application logic (single-file project)
└── README.md      # Project documentation
```

---

##  Installation & Setup

1. **Clone the repository**
```bash
   git clone [[https://github.com/<Jayyy-01>/student-placement-tracker.git]](https://github.com/Jayyy-01/student-placement-tracker.git)
```

2. **Navigate into the project folder**
```bash
   cd student-placement-tracker
```

3. **Run the application**
```bash
   python main.py
```

   > Requires Python 3.6 or higher. No external packages needed.

---

##  Usage

Once running, you'll see a menu-driven interface:

```
===== Student Placement Tracker =====
1. Add Student
2. Display All Students
3. Update Student Score
4. Change Platform
5. Show Total Students
6. Exit
Enter your choice:
```

### Adding a Student
Enter details in the format: `StudentID,Name,Branch,Score`

```
Enter student details: K101,Jayasree P,Python,85
Student added successfully.
```

### Viewing All Students

```
Student ID: K101
Name: Jayasree P 
Branch: Python
Mock Score: 85
Placement Status: Placement Ready
Platform: KodNest
```

### Placement Status Logic

| Mock Score Range | Status |
|---|---|
| 80 – 100 | Placement Ready |
| 60 – 79 | Needs More Practice |
| 0 – 59 | Not Ready |

---

##  Validation Rules

- **Duplicate IDs:** A student ID already in use cannot be re-added.
- **Score Range:** Scores must be between 0 and 100; invalid scores are rejected and the previous value is retained.

---

##  Testing

The application has been manually tested against the following scenarios:

- Adding multiple unique students
- Attempting to add a duplicate student ID
- Updating a score within a valid range
- Attempting an invalid score update (rejected, previous score retained)
- Updating a score for a non-existent student ID
- Changing the platform name and confirming it reflects across all profiles
- Selecting an invalid menu option
- Exiting the application cleanly

---


##  Author

**Jayasree P**
- GitHub: [@Jayyy-01](https://github.com/Jayyy-01)
---

## 📄 License

This project is open-source and available for educational use.
