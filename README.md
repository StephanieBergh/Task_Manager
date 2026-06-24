# Task Manager

## Project Overview

Task Manager is a command-line application written in Python that allows users to create, manage, edit, and track tasks. The system supports user authentication, task assignment, task completion tracking, report generation, and administrative functions.

The project demonstrates object-oriented programming principles, file handling, data validation, and modular software design.

---

## Features

### User Management

- User login and authentication
- Admin-only user registration
- Validation of usernames and passwords

### Task Management

- Create new tasks
- Assign tasks to registered users
- View all tasks
- View tasks assigned to the logged-in user
- Mark tasks as completed
- Edit task assignments
- Edit due dates

### Administrative Functions

Administrators can:

- Register new users
- Delete tasks
- View deleted tasks
- Generate reports
- Display task statistics

### Reporting

The application automatically generates:

- Task overview reports
- User overview reports

Reports include:

- Total tasks
- Completed tasks
- Incomplete tasks
- Overdue tasks
- User performance statistics

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- File Handling
- Datetime Module
- Tabulate Library

---

## Project Structure

```text
Task-Manager/
│
├── task_manager.py
├── user.txt
├── tasks.txt
└── README.md
```

---

## How It Works

### Login System

Users must log in using a valid username and password stored in `user.txt`.

### Task Assignment

Tasks contain:

- Assigned user
- Task title
- Task description
- Date assigned
- Due date
- Completion status

### Task Editing

Users can:

- Mark tasks as completed
- Change task ownership
- Update due dates

Completed tasks cannot be edited.

### Task Deletion

Deleted tasks are not permanently removed. They are moved to `bin.txt`, allowing administrators to review deleted records.

### Report Generation

The system generates:

#### Task Overview

- Total tasks
- Completed tasks
- Uncompleted tasks
- Overdue tasks
- Completion percentages

#### User Overview

- Total tasks per user
- Percentage of assigned tasks
- Percentage completed
- Percentage incomplete
- Percentage overdue

---

## Object-Oriented Design

The project uses a `Tasks` class to represent individual tasks.

### Task Attributes

- User
- Title
- Description
- Date Assigned
- Due Date
- Completion Status

### Task Methods

- `task_completed()`
- `__str__()`

This design improves code organization and maintainability.

---

## Skills Demonstrated

- Python Programming
- Object-Oriented Programming
- File Handling
- Exception Handling
- Input Validation
- Data Persistence
- Modular Programming
- Report Generation

---

## Future Improvements

Potential enhancements include:

- Graphical User Interface (GUI)
- Database integration using SQLite
- Password hashing for improved security
- Task search and filtering
- Task priority levels
- Email notifications for overdue tasks
- Task restoration from the recycle bin

---
## How to Run

### Prerequisites

Make sure Python 3 is installed on your system.

You can verify your installation by running:

```bash
python --version
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/StephanieBergh/python-task-manager.git
```

2. Navigate to the project folder:

```bash
cd python-task-manager
```

3. Install required packages:

```bash
pip install tabulate
```

### Running the Application

Run the program from the terminal:

```bash
python task_manager.py
```

### Default Admin Login

The application requires a valid username and password stored in `user.txt`.

Example:

```text
Username: admin
Password: adm1n
```

*(Use the credentials stored in your `user.txt` file.)*
## Author

**Stephanie Bergh**

Junior Data Analyst | Python Developer

GitHub: https://github.com/StephanieBergh

LinkedIn: https://www.linkedin.com/in/stephanie-bergh-142aa818a/

---
