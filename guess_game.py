# Guess Secret number Game
print('''Hey! buddy let play game!
I have secret number i want you to guess the number.
NB: you've only 3 attempt ''')
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    user_input = input("Guess the secret number ")
    guess_count += 1
    if user_input == secret_number:
        print("You Won!")
        break
    elif guess_count < guess_limit:
        print("try again!")
else:
    print(f"Sorry, you failed the secret number is {secret_number}")