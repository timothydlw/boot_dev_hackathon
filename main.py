import questionary #imports the questionary library for interactive command line prompts
from constants import * #imports constants from the constants.py file for use in calculations
import time #imports the time library to add a delay for user experience

#converts user age input into float so inputs can be used in calculations
def get_float_input(prompt):
    return float(input(prompt))

#determines which BMR calculation to use based on user gender
def calculate_bmr(gender, weight, height, age):
    if gender.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

#returns the activity multiplier based on user-selected activity level
def get_activity_multiplier(activity_level):
    return {
        "Sedentary: little or no exercise": sedentary,
        "Light: exercise 1-3 times per week": lightly_active,
        "Moderate: exercise 4-5 times per week": moderately_active,
        "Very Active: intense exercise 6-7 days per week": very_active,
        "Extra Active: very intense exercise daily or physical job": extra_active
    }[activity_level]

#returns the goal modifier based on user-selected goal
def get_goal_modifier(goal):
    return {
        "Weight Loss": weight_loss,
        "Weight Maintenance": weight_maintenance,
        "Weight Gain": weight_gain
    }[goal]

#main function asks for user metrics to calculate daily calorie needs
def main():
    print("Welcome to my calorie calculator!\n")
    age = get_float_input("Please enter your age in years: ")
    #questionary creates a dropdown to avoid spelling errors and ensure consistent input
    gender = questionary.select("Please select your gender:", choices=["Male", "Female"]).ask()
    height_units = questionary.select(
        "Please select your height units:",
        choices=["Centimeters (cm)", "Feet and Inches (ft/in)"]
    ).ask()
    #converts height units for ease of use
    if height_units == "Centimeters (cm)":
        height = get_float_input("Please enter your height in cm: ")
    else:
        feet = get_float_input("Please enter your height in feet: ")
        inches = get_float_input("Please enter your height in inches: ")
        height = convert_to_cm(feet, inches)
    weight_units = questionary.select(
        "Please select your weight units:",
        choices=["Kilograms (kg)", "Pounds (lbs)"]
    ).ask()
    weight = get_float_input("Please enter your weight: ")
    #allows for weight conversion for ease of use
    if weight_units == "Pounds (lbs)":
        weight = convert_to_kg(weight)
    activity_level = questionary.select(
        "Please select your activity level:",
        choices=[
            "Sedentary: little or no exercise",
            "Light: exercise 1-3 times per week",
            "Moderate: exercise 4-5 times per week",
            "Very Active: intense exercise 6-7 days per week",
            "Extra Active: very intense exercise daily or physical job"
        ]
    ).ask()
    goal = questionary.select(
        "Please select your goal:",
        choices=["Weight Loss", "Weight Maintenance", "Weight Gain"]
    ).ask()

    bmr = calculate_bmr(gender, weight, height, age)
    activity_multiplier = get_activity_multiplier(activity_level)
    goal_modifier = get_goal_modifier(goal)
    #determines how to use the goal modifer because the weight gain modifier is added, while the others are multiplied
    if goal == "Weight Gain":
        calories = bmr * activity_multiplier + weight_gain
    else:
        calories = bmr * activity_multiplier * goal_modifier

    # .0f formats the weight float to 0 decimal places for readability
    print(f"\nYou have entered: {age} years, {gender}, {height} cm, {weight:.0f} kg, {activity_level}, {goal}")
    time.sleep(2)  # Wait for 2 seconds to simulate processing time
    print("Calculating your recommended daily calories...")
    time.sleep(2)  # Wait for 2 seconds to simulate processing time
    print(f"Your recommended intake is {calories:.0f} calories/day.") #.0f formats the calories float to 0 decimal places for readability

if __name__ == "__main__":
    main()