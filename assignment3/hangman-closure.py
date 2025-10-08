def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter.lower())

        display = ''.join([ch if ch.lower() in guesses else '_' for ch in secret_word])
        print(display)

        for char in secret_word:
            if char.lower() not in guesses:
                return False
        return True
    return hangman_closure

secret = input("Enter the secret word: ")

hangman = make_hangman(secret)

done = False
while not done:
    guess = input("Guess a letter: ")
    done = hangman(guess)

print("You got it! The word was", secret)