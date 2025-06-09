import random
import time

def choose_word():
    words = ['python', 'jargon', 'medium', 'jumble', 'horror']
    return random.choice(words)

def word_display(word, guesses):
    display_word = ''
    for char in word:
        if char in guesses:
            display_word += char + ' '
        else:
            display_word += '_ '
    return display_word.strip()

def winning_condition(word, guesses, turns):
    if all(char in guesses for char in word):
        return 1
    elif turns == 0:
        return 0

def start_game():
    name = input("What is your name? ")
    print(f"\nHello, {name}! Time to play Hangman!")
    time.sleep(1)
    print("Start guessing...\n")
    time.sleep(0.5)
    
def hangman_game():
    word = choose_word()
    turns = 6
    guesses = ''

    while turns > 0:
        print("\nYou have", turns, 'guesses remaining')
        print("Word:", word_display(word, guesses))
        print("Guessed letters:", ' '.join(sorted(set(guesses))))
        
        guess = input("\nGuess a character: ").lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet character.")
            continue

        if guess in guesses:
            print("You have already tried this letter.")
            continue
        else:
            guesses += guess

        if guess not in word:
            print("Wrong! Try again.")

        turns -= 1
        flag = winning_condition(word, guesses, turns)

        if flag == 1:
            print("\n🎉 You won!")
            print("You guessed the word:", word.upper())
            break
        elif flag == 0:
            print("\n You lose.")
            print("The correct word was:", word.upper())
            break

if __name__ == "__main__":
    start_game()
    while True:
        hangman_game()
        value = input("Will you play again ?(Yes/No):")
        if value.lower() == 'no':
            print("\nExiting...")
            print("GoodBye!")
            break