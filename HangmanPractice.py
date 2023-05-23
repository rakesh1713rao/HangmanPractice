import random
import hangman_words
import hangman_art
from replit import clear


print(hangman_art.logo)

# word_list = ["ardvark","baboon","camel"]
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

print(chosen_word)

display_word = []
for i in range(word_length):
    display_word += "_"



while end_of_game == False:
    guess_word = input("Guess the letter: ").lower()
    clear()

    if guess_word in display_word:
        print(f"You have already chosen this letter :{guess_word}")


    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current Position :{position}")
        if letter == guess_word:
            display_word[position] = letter
        
        
    if guess_word not in chosen_word:
        print(f"The letter'{guess_word}' is not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
               
        print(f"Lives Left = {lives}")
        print(hangman_art.stages[lives])

    print(f"{' '.join(display_word)}")  #Join all the elements in the list and turn it into a String.

    if "_" not in display_word:
        end_of_game = True
        print("You Win!!")






# for i in chosen_word:
#     if i == guess_word:
#         print("Right")
#     else:
#         print("Wrong")