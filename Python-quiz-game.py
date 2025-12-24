#python quiz game
from requests import options

questions = ("What is the largest planet in our solar system?:  ",
           "What is the chemical symbol of gold?:  ",
           "Who was the first president of the United States?:  ",
           "Which country has the most official languages?:  ",
           "Which movie won the Academy Award for Best Picture in 1994?:  ",
           "Who wrote the novel 1984?:  ")
options = (("A. Earth","B. Jupiter","C. Saturn","D. Mars"),
           ("A. Au","B. Ag","C. Pb","D. Fe"),
           ("A. George Washington","B. Abraham Lincoln","C. Thomas Jefferson","D. John Adams"),
           ("A. India","B. Switzerland","C. South Africa","D. Canada"),
           ("A. Forrest Gump","B. The Shawshank Redemption","C. Pulp Fiction","D. Schindler's List"),
           ("A. Aldous Huxley","B. George Orwell","C. J.R.R Tolkien","D. F. Scott Fitzgerald"))
answers = ("B", "A", "A", "C", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D):  ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("-------------------------")
print("     RESULTS     ")
print("-------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()


print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")