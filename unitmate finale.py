import time
import random
import calendar
import datetime

# --- DATA STORAGE ---
tasks = [] 
goals = ["Pass Sem 1 with distinction", "Learn Python"] 

# --- MODULE 1: TASK MANAGER ---
def add_task():
    print("\n--- Add New Task ---")
    title = input("Enter Task Title: ")
    due_date = input("Enter Due Date (DD/MM): ")
    
    task = {
        "title": title,
        "due": due_date,
        "status": "Pending"
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    print("\n--- Your Schedule ---")
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['title']} (Due: {task['due']}) - [{task['status']}]")

def mark_complete():
    view_tasks()
    if tasks:
        try:
            # .strip() removes accidental spaces
            val = input("\nEnter task number to mark complete: ").strip()
            task_num = int(val) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]['status'] = "Completed"
                print("Task updated!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

# --- MODULE 2: FOCUS TIMER ---
def focus_timer():
    print("\n--- Focus Hub ---")
    try:
        val = input("Enter study time in minutes: ").strip()
        minutes = int(val)
        seconds = minutes * 60
        
        print(f"Timer started for {minutes} minutes. Focus now!")
        
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer_format = '{:02d}:{:02d}'.format(mins, secs)
            print(timer_format, end='\r') 
            time.sleep(1)
            seconds -= 1
            
        print("\nTime's up! Good job.")
        tips = ["Drink some water!", "Stretch your back!", "Look away from the screen."]
        print(f"Wellness Tip: {random.choice(tips)}")
        
    except ValueError:
        print("Please enter a valid number.")

# --- MODULE 3: CALENDAR ---
def view_calendar():
    print("\n--- Calendar View ---")
    now = datetime.datetime.now()
    yy = now.year
    mm = now.month
    
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_str = cal.formatmonth(yy, mm)
    print(month_str)
    
    check_other = input("Check a specific month? (y/n): ").strip()
    if check_other.lower() == 'y':
        try:
            y_input = int(input("Enter Year (e.g. 2025): "))
            m_input = int(input("Enter Month (1-12): "))
            print(calendar.month(y_input, m_input))
        except ValueError:
            print("Invalid input.")

# --- MODULE 4: GOAL MANAGER (FIXED) ---
def manage_goals():
    while True:
        print("\n" + "-"*20)
        print(" GOAL LOCKER ")
        print("-" * 20)
        
        # Display goals with clear numbers
        if not goals:
            print("No goals set yet.")
        else:
            for i, g in enumerate(goals):
                print(f"[Goal {i+1}]: {g}")
        
        print("\nMENU:")
        print("1. Add Goal")
        print("2. Edit Goal (Overwrite)")
        print("3. Delete Goal")
        print("4. Back to Main Menu")
        
        choice = input("Choice: ").strip() # Removes spaces
        
        if choice == '1':
            new_goal = input("Enter new goal: ")
            goals.append(new_goal)
            print("Saved!")
            
        elif choice == '2': # The Edit Feature
            if not goals:
                print("Nothing to edit.")
                continue
            try:
                # Ask for the NUMBER, not the name
                idx_input = input("Enter the Goal NUMBER to edit (e.g., 1): ").strip()
                idx = int(idx_input) - 1
                
                # Check if that number exists
                if 0 <= idx < len(goals):
                    print(f"--> You are changing: '{goals[idx]}'")
                    new_text = input("Enter the NEW text: ")
                    goals[idx] = new_text
                    print("Update successful!")
                else:
                    print("Error: That number is not on the list.")
            except ValueError:
                print("Error: Please enter a number (1, 2, 3...), not text.")
                
        elif choice == '3': # The Delete Feature
            if not goals:
                print("Nothing to delete.")
                continue
            try:
                idx_input = input("Enter Goal NUMBER to remove: ").strip()
                idx = int(idx_input) - 1
                if 0 <= idx < len(goals):
                    removed = goals.pop(idx)
                    print(f"Deleted: '{removed}'")
                else:
                    print("Error: Invalid number.")
            except ValueError:
                print("Error: Please enter a number.")
                
        elif choice == '4':
            break 
        else:
            print("Invalid choice.")


# --- DASHBOARD ---
def dashboard():
    print("\n" + "="*30)
    print(" UNIMATE DASHBOARD ")
    print("="*30)
    
    print("GOALS (Top 3):")
    if not goals:
        print("  (No goals set)")
    else:
        for goal in goals[:3]: 
            print(f"* {goal}")
    if len(goals) > 3: print("... (Select 'Manage Goals' to see more)")
    
    pending_count = sum(1 for t in tasks if t['status'] == "Pending")
    print(f"\nYou have {pending_count} pending tasks.")
    
    print("\n1. View/Manage Schedule")
    print("2. Start Focus Timer")
    print("3. View Calendar")
    print("4. Manage Goals") 
    print("5. Exit")


# --- MAIN EXECUTION ---
def main():
    while True:
        dashboard()
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            print("\n1. View Tasks\n2. Add Task\n3. Mark Complete")
            sub_choice = input("Choice: ").strip()
            if sub_choice == '1': view_tasks()
            elif sub_choice == '2': add_task()
            elif sub_choice == '3': mark_complete()
            
        elif choice == '2':
            focus_timer()

        elif choice == '3':
            view_calendar()
            
        elif choice == '4':
            manage_goals() 
            
        elif choice == '5':
            print("Goodbye! Keep studying.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "_main_":
    main()
    main()
