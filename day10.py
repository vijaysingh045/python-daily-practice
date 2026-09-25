questions = [
    "What is the capital of India?",
    "Which language are we learning?",
    "How many days are there in a week?",
    "What is 10 + 20?",
    "Which keyword is used to define a function in Python?"
]

answers = [
    "delhi",
    "python",
    "7",
    "30",
    "def"
]

score = 0

print("===== PYTHON QUIZ =====")

for i in range(len(questions)):

    print("\nQuestion", i + 1)
    print(questions[i])

    user_answer = input("Your answer: ").lower()

    if user_answer == answers[i]:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong ❌")
        print("Correct answer:", answers[i])

print("\n===== RESULT =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100

print("Percentage:", percentage, "%")

if percentage == 100:
    print("Excellent! 🏆")
elif percentage >= 60:
    print("Good Job! 👍")
elif percentage >= 40:
    print("Keep Practicing! 💪")
else:
    print("Need More Practice! 📚")