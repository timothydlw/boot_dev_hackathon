import questionary #imports the questionary library for interactive command line prompts
from constants import * #imports constants from the constants.py file for use in calculations
import time #imports the time library to add a delay for user experience

#converts user inputs into floats so inputs can be used in calculations and adds error handling if inputted values are negative not not numbers
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

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

#calculates daily protein needs based on user weight and units chosen in main function
def get_protein(weight, weight_units):
    if weight_units == "Kilograms (kg)":
        protein = weight * protein_per_kg
    else:
        protein = weight * protein_per_lb
    return protein

#calculates daily fats needs based on user weight and units chosen in main function
def get_fats(weight, weight_units):
    if weight_units == "Kilograms (kg)":
        fats = weight * fats_per_kg
    else:
        fats = weight * fats_per_lb
    return fats

#calculates daily carbohydrate needs based on user calories, protein, and fats
def get_carbs(cals, protein, fats):
    protein_calories = protein * 4  # 1 gram of protein = 4 calories
    fats_calories = fats * 9  # 1 gram of fat = 9 calories
    carbs_calories = cals - (protein_calories + fats_calories)
    carbs = carbs_calories / 4  # 1 gram of carbohydrate = 4 calories
    return carbs

#main function asks for user metrics to calculate daily calorie and macronutrient needs
def main():
    print("Welcome to my calorie and macronutrient calculator!\nPlease answer the following questions to get your daily calorie and macronutrient needs.\n")
    age = get_float_input("Please enter your age in years: ")
    
    #questionary creates a dropdown to avoid spelling errors and ensure consistent input
    gender = questionary.select("Please select your gender:", choices=["Male", "Female"]).ask()
    while gender is None: #error handling in case user cancels the questionary prompt
        print("Please make a selection.")
        gender = questionary.select("Please select your gender:", choices=["Male", "Female"]).ask()
    
    height_units = questionary.select(
        "Please select your height units:",
        choices=["Centimeters (cm)", "Feet and Inches (ft/in)"]
    ).ask()
    while height_units is None:
        print("Please make a selection.")
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
    
    #user inputs weight and selects units
    weight_units = questionary.select(
        "Please select your weight units:",
        choices=["Kilograms (kg)", "Pounds (lbs)"]
    ).ask()
    while weight_units is None:
        print("Please make a selection.")
        weight_units = questionary.select(
            "Please select your weight units:",
            choices=["Kilograms (kg)", "Pounds (lbs)"]
        ).ask()
    weight = get_float_input("Please enter your weight: ")
    
    #allows for weight conversion for ease of use
    if weight_units == "Pounds (lbs)":
        weight = convert_to_kg(weight)
        weight_units = "Kilograms (kg)"

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
    while activity_level is None:
        print("Please make a selection.")
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

    #user selects goal and error handling in case user cancels the questionary prompt
    goal = questionary.select(
        "Please select your goal:",
        choices=["Weight Loss", "Weight Maintenance", "Weight Gain"]
    ).ask()
    while goal is None:
        print("Please make a selection.")
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

    protein = get_protein(weight, weight_units)
    fats = get_fats(weight, weight_units)
    carbs = get_carbs(calories, protein, fats)

    # .0f formats the printed floats to 0 decimal places for readability
    print(f"\nYou have entered: {age} years, {gender}, {height:.0f} cm, {weight:.0f} kg, {activity_level}, {goal}")
    time.sleep(2)  # The 2 second timers are used to simulate processing time
    print("Calculating your recommended daily calories...")
    time.sleep(2)
    print(f"Your recommended intake is {calories:.0f} calories/day.")
    time.sleep(2)
    print("Calculating your recommended daily macronutrients...")
    time.sleep(2)
    print(f"Your recommended macronutrients are:\nProtein: {protein:.0f} grams/day\nFats: {fats:.0f} grams/day\nCarbohydrates: {carbs:.0f} grams/day")

if __name__ == "__main__":
    main()