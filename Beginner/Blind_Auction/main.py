from replit import clear
from art import logo

print(logo)

auction_running = True
auction_records = []
highest_bid = 0
highest_bidder = ""

while auction_running:
  
  bidder = {}
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))

  bidder["name"] = name
  bidder["bid"] = bid
  auction_records.append(bidder)
  
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  
  if more_bidders == "no":
    auction_running = False
    for person in range(len(auction_records)):
      if auction_records[person]["bid"] > highest_bid:
        highest_bid = auction_records[person]["bid"]
        highest_bidder = auction_records[person]["name"]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
  elif more_bidders == "yes":
    clear()
  