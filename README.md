# Task Management System (Python CLI)

A command-line task management system built in Python that allows users to manage tasks with authentication, assignment, tracking, reporting, and file-based data persistence.

This project simulates a real-world workflow system where users can log in, manage tasks, and generate performance reports.

---

##  Features

### User Management
- User authentication (login system)
- Admin-only user registration
- Username/password validation
- Secure username creation with duplicate prevention

### Task Management
- Add new tasks assigned to users
- View all tasks
- View tasks assigned to logged-in user
- Edit task details (user assignment, due date)
- Mark tasks as complete
- Delete tasks (admin only)

### Reporting System
- Generate task overview report
- Generate user performance reports
- Track:
  - Completed tasks
  - Overdue tasks
  - Task distribution per user
  - Completion percentages
  - 
### Data Persistence
- File-based storage using `.txt` files:
  - `user.txt`
  - `tasks.txt`
  - `bin.txt` (deleted tasks archive)
  - `program_start_info.txt`

---

##  Technologies Used

- Python 3
- File handling (read/write operations)
- Object-Oriented Programming (classes for Tasks)
- Date & time handling (`datetime`)
- Command-line interface (CLI)

---

## Project Structure
Task-Management-System/
│
├── task_manager.py # Main program logic
├── user.txt # Stored user credentials
├── tasks.txt # Active tasks
├── bin.txt # Deleted tasks archive
├── program_start_info.txt # Program run tracking
└── README.md

## How to Run

1. git clone https://github.com/StephanieBergh/Task_Manager.git
2. cd task-management-system
3. python task_manager.py

## Default Admin Access
Username: admin
Password: adm1n
