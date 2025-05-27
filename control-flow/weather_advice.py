#!/usr/bin/env python3
"""
Weather Recommendation Program
This script asks the user about current weather conditions
and provides clothing recommendations based on their input.
"""

def main():
    # Prompt user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ")
    
    # Provide clothing recommendations based on input
    if weather.lower() == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather.lower() == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather.lower() == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    main()

