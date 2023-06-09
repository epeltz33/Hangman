import random
import sys  


def greet_user():
    print("Welcome to Hangman!")
    print("You have 6 guesses to guess the word")
    print("Good Luck!")
    print(" ")


class Word:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed = set()
        self.guesses = 6
        self.letters = set(self.word)

    def print_word(self):
        for letter in self.word:
            print(letter if letter in self.guessed else "_", end=" ")
        print(" ")

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guessed:
            print("You already guessed that letter.")
        elif letter in self.letters:
            self.guessed.add(letter)
            print("Correct!")
        else:
            self.guesses -= 1
            self.guessed.add(letter)
            print("Wrong guess! Try again!")

        print(" ")

    def game_over(self):
        if self.guesses == 0:
            print(f"Game over! You lose!😭😭😭\nThe word was {self.word}\n")
            return True
        return False

    def game_won(self):
        if self.letters.issubset(self.guessed):
            print("Game over! You win!🎉🎉🎉\n")
            return True
        return False

    def play(self):
        greet_user()
        while True:
            self.print_word()
            print(f"You have {self.guesses} guesses left")
            print("Letters guessed: " + ', '.join(sorted(self.guessed)))
            letter = input("Guess a letter: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single letter.\n")
                continue
            self.guess_letter(letter)
            if self.game_over() or self.game_won():
                break
            print(" ")

        print("Thanks for playing!")
        print(" ")


def main():
    words = ["wristwatch", "jazz", "strength", "buzzing", "uptown", "lemons",
             "transcript", "president", "gossip", "guitar", "olympia", "khakis"]
    word = random.choice(words)
    game = Word(word)
    game.play()

    # Prompt the user to play again or exit
    while True:
        play_again = input("Would you like to play again? (Y/N): ").lower()
        if play_again in ["y", "n"]:
            break
        else:
            print("Please enter 'Y' for yes or 'N' for no.")
    if play_again == "y":
        main()
    else:
        print("Goodbye!")
        sys.exit()  # Use sys.exit() to terminate the program


if __name__ == "__main__":
    main()
