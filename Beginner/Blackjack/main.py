from replit import clear
import random
from art import logo


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  choice = random.choice(cards)
  return choice


def calculate_score(cards_list):
  """Takes a list of cards and return the score calculated from the cards"""
  if len(cards_list) == 2 and sum(cards_list) == 21:
    return 0
  
  if 11 in cards_list and sum(cards_list) > 21:
    cards_list.remove(11)
    cards_list.append(1)
  return sum(cards_list)


def compare(player_score, computer_score):
  
  if player_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  elif player_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif player_score == 0:
    return "Win with a Blackjack 😎"
  elif player_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif player_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def play_game():
  print(logo)
  player_cards = []
  computer_cards = []
  game_over = False
  
  for i in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while not game_over:  
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if player_score == 0 or computer_score == 0 or player_score > 21:
      game_over = True
    else:
      user_keep_dealing = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_keep_dealing == 'y':
        player_cards.append(deal_card())  
      else:
        game_over = True
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"  Your final hand: {player_cards}, final score: {player_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(player_score, computer_score))

  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()