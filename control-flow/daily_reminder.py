#!/usr/bin/env python3
"""
Personal Daily Reminder
This script provides a customized reminder for a single task based on
its priority level and time sensitivity.
"""

def main():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Process task based on priority and time sensitivity using match-case
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Plan to complete it soon.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Try to work on it this week.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print(f"Note: '{task}' has been added to your tasks.")

if __name__ == "__main__":
    main()

