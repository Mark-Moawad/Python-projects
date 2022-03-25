import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list

stages = hangman_art.stages


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []

for i in range(word_length):
  display += "_"

# for Testing:
# print(f"Pssst, the solution is {chosen_word}")

number_of_lives = 6
end_of_game = False
guessed_letters = []

print(hangman_art.logo)

while not end_of_game:
  output_word = ""
  guess = input("Guess a letter: ").lower()
  
  for position in range(word_length):
    if chosen_word[position] == guess:
      display[position] = guess
      
  for letter in range(word_length):
    output_word += display[letter]
  print(output_word)      
  
  if guess not in chosen_word:
    print(f"\n{guess} is not a letter in the word, you lose a life!")
    if guess in guessed_letters:
      print(f"\nYou have guessed '{guess}' before!")
    else:
      guessed_letters += guess
      number_of_lives -= 1
      
    if number_of_lives == 0:
      end_of_game = True
      print("\nGame over!")
      print(f"\nThe word is: {chosen_word}")
  print(f"\nlives remaining: {number_of_lives}")
  
  if "_" not in display:
    end_of_game = True
    print("\nYou win!")
    
  print(stages[number_of_lives])