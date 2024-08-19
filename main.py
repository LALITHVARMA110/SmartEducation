import random

# Dictionary of states and their capitals
states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Maharashtra": "Mumbai",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Gujarat": "Gandhinagar",
    "Uttar Pradesh": "Lucknow",
    "West Bengal": "Kolkata",
    "Rajasthan": "Jaipur",
    "Punjab": "Chandigarh",
    "Haryana": "Chandigarh",
    # Add more states and capitals as needed
}

def quiz():
    score = 0
    total_questions = 5  # Number of questions in the quiz

    print("Welcome to the States and Capitals Quiz!")
    print(f"You will be asked {total_questions} questions.")

    states = list(states_and_capitals.keys())
    
    for _ in range(total_questions):
        state = random.choice(states)
        answer = input(f"What is the capital of {state}? ")

        if answer.strip().lower() == states_and_capitals[state].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {states_and_capitals[state]}.")

    print(f"Quiz Over! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    quiz()
