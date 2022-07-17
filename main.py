import random
#It will import the word list from hangman_words
from hangman_words import word_list
#It will import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#word_list = ["ardvark", "baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word) #this is the length of ramdom chonsen word
lives = 6
print(f'Pssst, the solution is {chosen_word}.')
#create blanks
display=[]

for _ in range(word_length):
    display += "_"
#print(display)
end_of_game = False
while not end_of_game:
    guess=input("Guess a Letter").lower()

    if guess in display:
        print(f"you already guessed: {guess}")
#check the guessd letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
#check if the user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")


#check if the user has got  all letter
    if "_" not in display:
        end_of_game = True
        print("you win")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    # It will import the ASCII from hangman_art.py and print it in the game.
    from hangman_art import stages
    print(stages[lives])

print(f"The Real word is: {chosen_word}")

