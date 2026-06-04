# ===== Importing external modules ===========
'''This is the section where you will import modules'''
from tabulate import tabulate
from datetime import date
from datetime import datetime

# CLASSES

class Tasks():

    def __init__(self, user, title, description, today, due, status):
        self.user = user
        self.title = title
        self.description = description
        self.today = today
        self.due = due
        self.status = status

    def task_completed(self):
        self.status = "Yes"
    
    def __str__(self):
        
        return f"{self.user}, {self.title}, {self.description}, {
            self.today}, {self.due}, {self.status}"


# FUNCTIONS
user_list = []
task_list = []
deleted_list = []

def read_users():
    '''
    Reads the registered user usernames and passwords 
    from "user.txt" and saves to user_list.
    '''

    user_list.clear()
    try:
        with open("user.txt", "r") as file:
            for line in file:
                line = line.strip()
                user_list.append(line.split(", "))

    except FileNotFoundError:
        print("Error: The file was not found.")
    
    return


def read_tasks():
    '''
    Reads the tasks from "tasks.txt" and saves to task_list.
    '''

    task_list.clear()
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                attributes = line.split(", ")
                task_list.append(Tasks((attributes[0]).strip(), 
                                       attributes[1].strip(), 
                                        attributes[2].strip(), 
                                        attributes[3].strip(), 
                                        attributes[4].strip(), 
                                        attributes[5].strip()))

    except FileNotFoundError:
        print("Error: The file was not found.")
    
    return


def read_bin():
    '''
    Reads deleted tasks from the "bin.txt" and saves
    to "deleted_list".
    '''

    deleted_list.clear()

    try:
        with open("bin.txt", "r") as file:
            for line in file:
                attributes = line.split(", ")
                deleted_list.append(Tasks((attributes[0]).strip(), 
                                          attributes[1].strip(), 
                                          attributes[2].strip(), 
                                          attributes[3].strip(), 
                                          attributes[4].strip(), 
                                          attributes[5].strip()))

    except FileNotFoundError:
        print("Error: The file was not found.")
    
    return


def store_info():
    '''
    Stores the number of tasks at the start of each program run 
    in "program_start_info".
    '''

    read_tasks()
    
    with open("program_start_info.txt", "a") as file:
        file.write(f"number of tasks at the start of the program run "
                   f"{datetime.today()}:\n{len(task_list)}\n")
    return


def check_username(username):
    '''
    Check the username against approved usernames in user_list.

    Argument: 
        username(str): User input username.

    Return: 
        bool: 
            True when username is listed in user_list.
            False otherwise.
        index (int): 
            Index of the username in user_list.
   '''
    
    for user in user_list:
        if user[0] == username:
            index = user_list.index(user)
            return True, index
    
    return False, -1


def check_password(password, index):
    '''
    Check the password against opproved passwords in user_list.

    Parameters: 
        password(str): User input password.
        index(int): username index.

    Return: 
        bool: 
            True if password is correct.
            False otherwise.
    '''

    if 0 <= index < len(user_list):
        return user_list[index][1] == password
    return False


def reg_user():
    '''
    Adds new user to "user.txt" and user_list with user input.
    '''

    # Only admin has access to register new users.
    print("Enter -1 anytiime to discard and return to menu")
    if username == "admin": 
        print("Please enter the new user information.") 
        while True:
            new_username = input("Username: ")
            
            # Check that user input is not empty.
            if not new_username:
                print("\nInput is empty. Please enter a username.")
           
            # Users cannot have the same username. This code checks if
            # the username has already been assigned.
            elif any(user[0] == new_username for user in user_list):
                print("\nUsername already exists. Please choose another.\n")
            
            elif new_username == "-1":
                return
            else:
                break
     
    if username == "admin":
        
        while True:
            new_password = input("Password: ")
            
            # Check that user input is not empty.
            if not new_password:
                print("\nInput is empty. Please enter a password.")
            
            elif new_password == "-1":
                return

            else: 
                password_check = input("Confirm new password: ")
            
                if new_password == password_check:
                    
                    # Saving new user details to txt file.
                    with open("user.txt", "a") as file:
                        file.write(f"\n{new_username}, {new_password}")
                    read_users()
                    break

                else:
                    print("\nPasswords do not match. Please try again.\n")
    else:
        print("Your profile is not authorized to register users.\n")

    if username == "-1":
        return


def add_task():
    '''
    Adds new task to "tasks.txt" and task_list using user input.
    '''

    while True:
        for_user = input("Username of user that task is assigned to: ")
        
        # Code ensures that the user that the task is assigned to, has
        # already been added to user_list.
        if any(user[0] == for_user for user in user_list):
            break
        
        elif for_user == "-1":
            return 
        else:
            print("\nUser not found. Please register user.")
            print("Enter -1 to return to menu.")
            
   
    # Ensure that input is received.
    while True:
        title = input("Title of task: ")
    
        if not title:
            print("\nInput is empty. Please enter the title of the task.")
            
        else:
            break
    
    # Ensure that input is received.
    while True:
        description = input("Description of task: ")
        if not description:
            print("\nInput is empty. Please enter the description of " \
            "the task.")
        else:
            break

    today = date.today()

    while True:
        try:
            # Ensure that input is received.
            while True:
                due_input = input("Due date(format-> YYYY-MM-DD): ")
                if not due_input:
                    print("\nInput is empty. Please enter the due date" \
                    " of the task.")
            
                else:
                    break
            
            # Format date so that it can be compared as well as written to file.
            due_compare = date.strptime(due_input, "%Y-%m-%d")
            due_formatted = due_compare.strftime("%d %b %Y")
            today_formatted = today.strftime("%d %b %Y")
            
            if due_compare >= today:
                break
            
            print("\nThe due date has already passed.")
            continue

        except ValueError:
            print("\nIncorrrect date format. Correct format: Year-Month-Day")
    
    default_status = "No"
    
    # Save new task to "task.txt" file.
    with open("tasks.txt", "a") as file:
        file.write(f"\n{Tasks(for_user.strip(), 
                                title.strip(), 
                                description.strip(), 
                                today_formatted, 
                                due_formatted, 
                                default_status.strip())}")
    # Update task_list
    read_tasks()


def view_one(list, index):
    '''
    Displays a task in a neat format.

    Arguments:
        list (list):
            The list where the object is stored.
        index (int):
            The index of the object to display.
    '''

    print("~"*60)
    if list != deleted_list:
        print(f"Task ID: {index+1}")
    print(f"{'Task:':20}{list[index].title}")
    print(f"{'Assigned to:':20}{list[index].user}")
    print(f"{'Date assigned:':20}{list[index].today}")
    print(f"{'Due date:':20}{list[index].due}")
    print(f"{'Task complete?':20}{list[index].status}")
    print(f"Task description:\n {list[index].description}")
    print("~"*60)


def view_all():
    '''
    Displays all of the tasks in task_list.
    '''

    # Using function view_one() to print one task at a time.
    for i, task in enumerate(task_list):
        view_one(task_list, i)    


def change_user(index):
    '''
    Changes the user to which the task is assigned to.
    
    Arguments:
        index (int):
            Index of the task that should be edited.
    '''

    username_change = input("Enter the new username: ")
    task_list[index].user = (username_change.strip())


def change_due_date(index):
    '''
    Changes the task due date.
    
    Arguments:
        index (int):
            Index of the task that should be edited.
    '''
        
    while True:    
        due_change = input("Enter the new due date "
                            "(Format: YYYY-MM-DD): ")
        
        # Check if new due date has not yet passed.
        due_compare = date.strptime(due_change, "%Y-%m-%d")
        today = date.today()
        
        if due_compare >= today:
            break
        
        print("\nThe new due date has already passed.")
        continue
        
    due_formatted = due_compare.strftime("%d %b %Y")
    task_list[index].due = due_formatted


def get_valid_task_number(valid_range):
    '''
    Ensures a valid user input

    Arguments:
        valid_range (list):
            list containg the valid inputs.
    '''

    user_input = (input("\nEnter '-1' to return to menu.\n"
            "Alternatively, enter the number of the task you want " \
            "to edit: "))
    
    while True:
        if user_input == "-1":
            return -1 
        
        try:
            index = int(user_input)-1

            if index in valid_range:
                view_one(task_list, index)
                return index

            else:
                print("\nInvalid input. Task ID not accepted.")
                return get_valid_task_number(valid_range)

        except ValueError:
            user_input = input("\nInvalid input. Please enter a " \
            "number.\n: ")


def view_mine():
    '''
    Displays only the tasks of the user that logged in 
    and allows user to edit these tasks.
    '''
    
    valid_range = []
    
    # Using function view_one() to display the users tasks.
    for i, task in enumerate(task_list):
        
        if task.user == username: 
            view_one(task_list, i)
            valid_range.append(i)
    
    index = get_valid_task_number(valid_range)
     
    if index == -1:
        return
    
    else:
        while True:
                        
            try:
                print("You have chosen to edit the tasks shown above.\n"
                    "To set the task status to completed, enter 0\n"
                    "To edit the username, enter 1\n"
                    "To edit the due date, enter 2\n" \
                    "To exit: enter -1\n")
                
                user_edit = int(input(": "))
                
                # Set task as completed.
                if user_edit == 0:
                    task_list[index].task_completed()
                    view_one(task_list, index)
                    break
                
                elif user_edit == -1:
                    return

                # Editing task if task has not been completed.
                if task_list[index].status == "No":
                    
                    # Editing task user
                    if user_edit == 1:
                        change_user(index)
                        view_one(task_list, index)
                        break
                    
                    # Editing task due date
                    elif user_edit == 2:
                        change_due_date(index)
                        view_one(task_list, index)
                        break     

                else:
                    print("\nInvalid input. You cannot edit completed " \
                    "tasks.")

            except ValueError:
                print("\nInvalid input.") 
                    
        # Saving changes to "task.txt" 
        with open("tasks.txt", "w") as file:
                pass

        for task in task_list:
            with open("tasks.txt", "a") as file:
                file.write(f"{task}\n")

        # Removing extra \n at end of last line
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
        if lines:
            lines[-1] = lines[-1].rstrip("\n")
        with open("tasks.txt", "w") as file:
            file.writelines(lines)
        
        # Saving changes to task_list
        read_tasks()


def view_completed():
    '''
    Displays deleted tasks from deleted_list.
    '''

    read_bin()
    for i in range (0,len(deleted_list)):
        view_one(deleted_list, i)
    
    if len(deleted_list) == 0:
        print("\nNo deleted items to show.\n")


def delete_task():
    '''
    Deletes a task using user input.
    '''

    view_all()

    while True:
        try:
            delete_ID = int(input("Enter the task ID that you would " \
            "like to delete: "))
            break
        except ValueError:
            print(f"\nInvalid entry. Please enter a number from 1 to "
                  f"{len(task_list)}")

    print("You want to delete:")
    index = delete_ID-1
    view_one(task_list, index)
    
    while True:
        go_on = input(f"\n\nAre you sure you want to delete task "
                      "with ID: " 
                  f"{delete_ID}? Enter Yes of No: ").lower()

        if go_on == "yes":

            try:
                with open("tasks.txt", "r") as file:
                    lines = file.readlines()

                # Storing deleted task in "bin.txt" 
                with open("bin.txt", "a") as file:
                    file.write(f"{task_list[index]}\n") 

                if lines:
                    lines.pop(index)
                
                # Remove new line character at the end of the 
                # last line in the file to prevent future issues 
                # from accuring..
                lines[-1] = lines[-1].rstrip("\n")

                with open("tasks.txt", "w") as file:
                    file.writelines(lines)
                
                # Save chenges to task_list and deleted_list
                read_tasks()
                read_bin()
                  
            except FileNotFoundError:
                print("\nError: The file was not found.")           
            break

        elif go_on == "no":
            print("\nNo tasks were deleted.\n")
            return
        else:
            print("\nInvalid entry. Please enter 'Yes' or 'No'")


def count_completed():
    '''
    Counts the number of completed tasks.

    Return:
        total_completed (int): 
            The number of completed tasks.
    '''

    total_completed = 0
    # The number of completed tasks that has already been deleted, 
    # will also be included in the count.
    for task in task_list:
        if task.status == "Yes":
            total_completed =+ 1
    for task in deleted_list:
        if task.status == "Yes":
            total_completed =+ 1
    return total_completed


def count_total():
    '''
    Counts the total number of tasks (including deteled tasks)
    
    Return:
        total_tasks (int): 
            the number of tasks in task_list and deleted_list.
    '''

    total_tasks = len(task_list) + len(deleted_list)
    return total_tasks


def check_overdue(task):
    '''
    Checks whether a task is overdue.

    Argument:
        task (object): a task object.
    
    Return: 
        bool:
            True if the task is overdue.
            False otherwise.
    '''
    
    if task.status == "No":
        due_date = datetime.strptime(task.due, "%d %b %Y").date() 
            
        if due_date < date.today():
            return True
    
    return False
    

def count_overdue():
    '''
    Counts the amount of overdue tasks in task_list.

    Return:
        total_overdue (int):
            Total number of overdue tasks in task_list.
    '''
    
    total_overdue = 0
    
    for task in task_list:
        
        if check_overdue(task):
            total_overdue = total_overdue + 1

    return total_overdue


def new_tasks():
    '''
    Calculates the total new tasks added using task.manager.py.

    Return:
        new_tasks (int):
            Number of new tasks added using the program.
    '''

    try:
        with open("program_start_info.txt","r") as file:
            lines = file.readlines()
            start_number = lines[1]  

    except FileNotFoundError:
        print("Error: The file was not found.")
    
    new_tasks = count_total()-int(start_number)
    return new_tasks


def report_per_user(user):
    '''
    Generates report info regarding a user.

    Arguments:
        user (str):
            The user for which the information should be generated.

    Return:
        user_tasks(int):
            Number of tasks assigned to user.
        percentage_tasks (int):
            Percentage of total tasks assigned to user.
        percentage_completed (int):
            Percentage of tasks assigned to user that has been 
            completed.
        percentage_uncompleted (int):
            Percentage of tasks assigned to user that has not been 
            completed.
        percentage_overdue (int):
            Percentage of tasks assigned to user that has not been 
            completed and is overdue.
    '''

    user_tasks = 0
    user_completed = 0
    user_overdue = 0

    for task in task_list:
        # Only looking at the tasks assigned to user.
        if task.user == user:
            user_tasks = user_tasks + 1
            
            # Calculates the number of completed tasks.
            if task.status == "Yes":
                user_completed = user_completed + 1
            
            # Calculates the amount of overdue tasks.
            elif task.status == "No":
                if check_overdue(task):
                    user_overdue = user_overdue + 1
        continue

    total = len(task_list)
    percentage_tasks = user_tasks/total*100
    
    if user_tasks > 0:
        percentage_completed = user_completed/user_tasks*100
        percentage_uncompleted = (user_tasks-user_completed)/user_tasks*100
        percentage_overdue = user_overdue/user_tasks*100
    
    else:
        percentage_completed = 0
        percentage_uncompleted = 0
        percentage_overdue = 0

    return (user_tasks, percentage_tasks, percentage_completed, 
            percentage_uncompleted, percentage_overdue)


def reports(): 
    '''
    Generates user and task reports as txt files.
    '''

    read_tasks()
    uncomplete = count_total() - count_completed()

    # Generating task report
    with open("task_overview.txt", "w") as file:   
        
        # Number of tasks generated using only this program.
        # This excludes tasks already assigned using txt file.
        file.write(f"The total number of tasks generated: "
                   f"{new_tasks()}\n")
        
        file.write(f"The total number of completed tasks: "
                   f"{count_completed()}\n")
        
        file.write(f"The total number of uncompleted tasks: "
                   f"{uncomplete}\n")
        
        file.write(f"The total number of uncompleted overdue tasks: "
                   f"{count_overdue()}\n")
        
        file.write(f"Incomplete tasks: "
                   f"{uncomplete/count_total()*100:.0f}%\n")
        
        file.write(f"Overdue tasks: "
                   f"{count_overdue()/count_total()*100:.0f}%\n")

    # Generating user report
    with open("user_overview.txt", "w") as file:
        file.write(f"The total number of users: {len(user_list)}\n")
        
        # Number of tasks generated using only this program.
        # This excludes tasks already assigned using txt file.
        file.write(f"The total number of generated tasks: {new_tasks()}\n")
    
        for user in user_list:
            user = user[0]

            file.write(f"\n{user}:\n")

            file.write(f"Total tasks assigned to {user}: "
                       f"{report_per_user(user)[0]}\n")
            
            file.write(f"Percentage tasks assigned to {user}: "
                       f"{report_per_user(user)[1]: .0f}%\n")
            
            file.write(f"Percentage tasks completed by {user}: "
                       f"{report_per_user(user)[2]: .0f}%\n")
            
            file.write(f"Percentage tasks uncompleted by {user}: "
                       f"{report_per_user(user)[3]: .0f}%\n")
            
            file.write(f"Percentage tasks overdue by {user}: "
                       f"{report_per_user(user)[4]: .0f}%\n")


def display_report():
    '''
    Displays task and user reports.
    '''
    
    #generating reports
    reports()

    print("\n\033[1mTASK OVERVIEW:\033[0m")
    with open("task_overview.txt", "r") as file:
        lines=file.readlines()

        for line in lines:
            print(line.strip())
      
    print("\n\033[1mUSER OVERVIEW:\033[0m")
    with open("user_overview.txt", "r") as file:
        lines=file.readlines()
        
        for line in lines:
            print(line.strip())
    
    print("\n")


# ==== Login Section ====

# Read username file:
read_users()
store_info()

# Creating a bin file:
with open("bin.txt","a") as file:
    pass

# Login
print("\033[1mTASK MANAGER LOGIN:\033[0m")
status = False
resume = 1   

# Getting user input and using comparing functions to determine authorization
while not status:
    username = input("Username: ")
    user_found, index = (check_username(username))
      
    if not user_found:
        print("User not found")
        continue

    password = input("Password: ")
    status = check_password(password, index)

    if not status:
        print("Incorrect information. Please try again.")


while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    
    if username == "admin":
        menu = input(
            '''Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        vc - view completed tasks
        del - delete tasks
        ds - display statistics
        gr - generate reports
        e - exit
        : '''
        ).lower()
    
    else:
        menu = input(
        '''Select one of the following options:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        : '''
    ).lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
        
    elif menu == 'vm':
        view_mine()

    elif menu == "vc" and username == "admin":
        view_completed()

    elif menu == "del" and username == "admin":
        delete_task() 

    elif menu == "gr" and username == "admin":
        reports()

    elif menu == "ds" and username == "admin":
        display_report()
    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")

    


