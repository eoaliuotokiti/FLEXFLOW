def get_workout_plan():
    # Dictionary mapping days to specific workouts
    plan = {
        "Monday": "Chest and Triceps - 3 sets of 12 reps",
        "Tuesday": "Back and Biceps - 3 sets of 12 reps",
        "Wednesday": "Active Recovery - 30 min light walk or yoga",
        "Thursday": "Shoulders and Abs - 4 sets of 10 reps",
        "Friday": "Leg Day - 4 sets of 8 reps",
        "Saturday": "Cardio - 45 min run or cycling",
        "Sunday": "Rest Day - Hydrate and recover!"
    }
    return plan

def main():
    print("--- Welcome to FlexFlow Workout ---")
    workout_plan = get_workout_plan()
    
    day = input("Enter a day of the week to see your plan: ").strip().capitalize()

    if day in workout_plan:
        print(f"\nYour plan for {day}:")
        print(f"-> {workout_plan[day]}")
    else:
        print("\nInvalid day. Please enter a full day name (e.g., Monday).")

if __name__ == "__main__":
    main()