#!/usr/bin/env python3
"""
Drawing Patterns with Nested Loops
This script draws a square pattern of asterisks (*) using
a while loop for rows and a for loop for columns.
"""

def main():
    try:
        # Prompt user for pattern size
        size = int(input("Enter the size of the pattern: "))
        
        # Validate input
        if size <= 0:
            print("Please enter a positive integer.")
            return
            
        # Draw the pattern using nested loops
        row = 0
        while row < size:
            # Print asterisks in a row using a for loop
            for col in range(size):
                print("*", end="")
            # Move to the next line after completing a row
            print()
            row += 1
            
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()

