import questionary
from constants import *

def main():
    print("Welcome to my calorie calculator!\nInput your age, gender, height, weight, activity level to get started, and goal to get started.")
    user_age = input("Please enter your age in years: ")
    #user_gender = input("Please enter your gender (male/female): ")
    user_gender = questionary.select(
        "Please select your gender:",
        choices=["Male", "Female"]
    ).ask()
    user_height = input("Please enter your height in cm: ")
    user_weight = input("Please enter your weight in kg: ")
    #user_activity_level = input("Please enter your activity level (sedentary/light/moderate/vigorous): ")
    user_activity_level = questionary.select(
        "Please select your activity level:",
        choices=["Sedentary: little or no exercise", "Light: exercise 1-3 times per week", "Moderate: exercise 4-5 times per week", "Very Active: intense exercise 6-7 days per week", "Extra Active: very intense exercise daily or physical job"]
    ).ask()
    user_goal = questionary.select(
        "Please select your goal:",
        choices=["Weight Loss", "Weight Maintenance", "Weight Gain"]
    ).ask()
    BMR_male = 10 * float(user_weight) + 6.25 * float(user_height) - 5 * float(user_age) + 5
    BMR_female = 10 * float(user_weight) + 6.25 * float(user_height) - 5 * float(user_age) - 161
    print(f"You have entered: {user_age} years, {user_gender}, {user_height} cm, {user_weight} kg, {user_activity_level} activity")
    print("Calculating your Basal Metabolic Rate (BMR)...")
    if user_gender == "male" and user_activity_level == "Sedentary: little or no exercise" and user_goal == "Weight Loss":
        user_BMR = (BMR_male * sedentary) * weight_loss
        print (f"Your BMR is {user_BMR} calories/day.")        
    else:
        print (f"Your BMR is {BMR_female} calories/day.")

if __name__ == "__main__":
    main()