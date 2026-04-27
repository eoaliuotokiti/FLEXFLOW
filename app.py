import random

def get_workout_plan():
    plan = {
        "Monday": [
            "Bench Press: 3 sets of 12",
            "Tricep Pushdowns: 3 sets of 15",
            "Incline Dumbbell Flyes: 3 sets of 12"
        ],
        "Tuesday": [
            "Pull-ups: 3 sets to failure",
            "Bicep Curls: 3 sets of 12",
            "Bent Over Rows: 4 sets of 10"
        ],
        "Wednesday": [
            "Yoga Flow: 20 minutes",
            "Light Walking: 15 minutes"
        ],
        "Thursday": [
            "Overhead Press: 4 sets of 10",
            "Lateral Raises: 3 sets of 15",
            "Plank: 3 sets of 1 minute"
        ],
        "Friday": [
            "Squats: 4 sets of 8",
            "Leg Curls: 3 sets of 12",
            "Calf Raises: 4 sets of 15"
        ],
        "Saturday": [
            "Running: 5km",
            "Stretching: 10 minutes"
        ],
        "Sunday": [
            "Rest and Recovery",
            "Hydration focus",
            "Meal prep for the week"
        ]
    }
    return plan

def get_daily_tip():
    tips = [
        "Drink at least 3 liters of water today.",
        "Ensure you get 8 hours of sleep for muscle recovery.",
        "Focus on your form rather than the weight.",
        "Consistency is more important than intensity.",
        "Don't forget to stretch after your workout."
    ]
    return random.choice(tips)

def calculate_bmi():
    print("\n--- FlexFlow BMI Calculator ---")
    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
        bmi = weight / (height ** 2)
        print(f"Your calculated BMI is: {bmi:.2f}")
    except ValueError:
        print("Please enter valid numbers for weight and height.")

def main():
    workout_plan = get_workout_plan()
    print("Welcome to FlexFlow: Your Personal Fitness Partner")
    
    while True:
        print("\nMain Menu:")
        print("1. View Workout Plan")
        print("2. Get a Daily Health Tip")
        print("3. BMI Calculator")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            day = input("Enter the day: ").strip().capitalize()
            if day in workout_plan:
                print(f"\nPlan for {day}:")
                for exercise in workout_plan[day]:
                    print(f"  * {exercise}")
            else:
                print("Invalid day entered.")
        elif choice == "2":
            print(f"\nToday's Tip: {get_daily_tip()}")
        elif choice == "3":
            calculate_bmi()
        elif choice == "4":
            print("Keep up the hard work! Goodbye.")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()