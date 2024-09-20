from posture_monitor import get_posture_data
from feedback_system import provide_feedback
from exercise_recommender import recommend_exercises
import time

def main():
    print("PosturePal monitoring started.")

    while True:
        # Get posture data from wearable device or simulated data
        posture_status = get_posture_data()

        # Provide real-time feedback based on posture data
        provide_feedback(posture_status)

        # Suggest exercises if posture needs improvement
        if posture_status == "poor":
            recommend_exercises()

        # Check posture every 5 seconds (simulation)
        time.sleep(5)

if __name__ == "__main__":
    main()


import random

def get_posture_data():
    """
    Simulates getting posture data from a wearable device.
    Returns either 'good' or 'poor' posture based on random data for demo purposes.
    """
    # Simulate posture data (e.g., from accelerometer in wearable device)
    posture = random.choice(["good", "poor"])
    
    print(f"Posture Status: {posture}")
    return posture





def provide_feedback(posture_status):
    """
    Provides real-time feedback based on the user's posture status.
    If posture is poor, a notification or haptic feedback will be triggered.
    """
    if posture_status == "good":
        print("You're maintaining good posture! Keep it up!")
    else:
        print("Warning: Poor posture detected. Please correct your posture.")

def recommend_exercises():
    """
    Recommends a personalized set of stretching exercises to help improve posture.
    """
    exercises = [
        "Shoulder rolls: Roll your shoulders forward and backward 10 times.",
        "Neck stretches: Slowly tilt your head to each side, holding for 10 seconds.",
        "Seated forward bend: Sit and reach for your toes, holding the stretch for 15 seconds.",
        "Spinal twist: Sit tall, twist gently to each side, holding for 10 seconds."
    ]

    print("Recommended Exercises:")
    for exercise in exercises:
        print(f"- {exercise}")

