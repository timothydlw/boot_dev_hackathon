def main():
    print("Welcome to my calorie calculator!\nInput your age, gender, height, weight, and activity level to get started.")
    user_age = input("Please enter your age in years: ")
    user_gender = input("Please enter your gender (male/female): ")
    user_height = input("Please enter your height in cm: ")
    user_weight = input("Please enter your weight in kg: ")
    user_activity_level = input("Please enter your activity level (sedentary/light/moderate/vigorous): ")
    print(f"You have entered: {user_age} years, {user_gender}, {user_height} cm, {user_weight} kg, {user_activity_level} activity")

if __name__ == "__main__":
    main()