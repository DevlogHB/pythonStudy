from art import logo;
import random;

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).



def check_answer(guess, answer):
    if guess > answer:
        print("Too high.");
    elif guess < answer:
        print("Too low.");
    else:
        print(f"You got it! The answer was {answer}");


def startGame():
    print("Welcom to the Number Guessing Game!");
    print("I'm thinking of a number between 1 and 100");
    chooseType = input("Choose a difficulty. Type 'easy' or 'hard' : ");
    print(logo);

    chanceNum = 10;

    if chooseType.lower() == "hard":
        chanceNum = 5;

    answer = random.randint(1,100);
    chooseNumber = 0;

    while chooseNumber != answer:
        print(f"You have {chanceNum} attempts remaining to guess the number");
        chooseNumber = int(input("Make a guess: "));
        check_answer(chooseNumber, answer);
        chanceNum -= 1;

        if chanceNum == 0:
            print(f"You've run out of guesses, you lose. (answer : {answer})");
            return;
        elif chooseNumber != answer:
            print("Guess again");

startGame();