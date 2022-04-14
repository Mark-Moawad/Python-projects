import random
import art
from game_data import data
from replit import clear

def select_comparables(data):
  """Selects a random value from a list"""
  return random.choice(data)

def format_data(comparable):
  """Formats a dictionary into a meaningful string"""
  name = comparable["name"]
  description = comparable["description"]
  country = comparable["country"]
  return f"{name}, a {description}, from {country}."

def compare(comp_A, comp_B):
  """Takes two comparables as arguments and returns which one has more followers on Instagram"""
  if comp_A["follower_count"] > comp_B["follower_count"]:
    return 'A'
  else:
    return 'B'

def play_game():
  current_score = 0
  game_over = False
  comparable_A = select_comparables(data)
  comparable_B = select_comparables(data)
  while comparable_A == comparable_B:
    comparable_B = select_comparables(data)
  print(art.logo)
  while not game_over:
    # # for debugging:
    # print(comparable_A)
    # print(comparable_B)
    # print(compare(comparable_A, comparable_B))
    # # debugging ends here
    print(f"Compare A: {format_data(comparable_A)}")
    print(art.vs)
    print(f"Against B: {format_data(comparable_B)}.")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer == compare(comparable_A, comparable_B):
      current_score += 1
      clear()
      comparable_A = comparable_B
      comparable_B = select_comparables(data)
      print(art.logo)
      print(f"You're right! Current score: {current_score}.")
    else:
      game_over = True
      clear()
      print(art.logo)
      print(f"Sorry, that's wrong. Final score: {current_score}")
    

play_game()