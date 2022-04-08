from random import randint
from art import logo
from replit import clear

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def check_answer(guess, answer, lives):
  """Checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return lives - 1
  elif guess < answer:
    print("Too low.")
    return lives - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty_level == "easy":
    return EASY_LEVEL_LIVES
  elif difficulty_level == "hard":
    return HARD_LEVEL_LIVES

def game():
  
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  answer = randint(1, 100)
  
  # # for debugging purpose
  # print(f"Pssst, the correct answer is {answer}")  
  
  lives = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {lives} attempt(s) remaining to guess the number.")
    
    guess = int(input("Make a guess: "))
    lives = check_answer(guess, answer, lives)
    if lives == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again!")
  
while(input("Do you want to play a game? 'y' or 'n': ") == 'y'):
  clear()
  game()