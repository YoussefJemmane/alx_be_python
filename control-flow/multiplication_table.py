#!/usr/bin/env python3
"""
Multiplication Table Generator
This script generates and prints the multiplication table for a given number
from 1 to 10 using a for loop.
"""

def main():
    try:
        # Prompt user for a number
        number = int(input("Enter a number to see its multiplication table: "))
        
        # Generate and print the multiplication table
        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

