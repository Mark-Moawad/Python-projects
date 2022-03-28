from replit import clear
from art import logo

print(logo)

# # The following solution works perfectly but integrates between Lists
# # and Dictionaries
# auction_running = True
# auction_records = []
# highest_bid = 0
# highest_bidder = ""

# while auction_running:
  
#   bidder = {}
#   name = input("What is your name?: ")
#   bid = int(input("What is your bid?: $"))

#   bidder["name"] = name
#   bidder["bid"] = bid
#   auction_records.append(bidder)
  
#   more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  
#   if more_bidders == "no":
#     auction_running = False
#     for person in range(len(auction_records)):
#       if auction_records[person]["bid"] > highest_bid:
#         highest_bid = auction_records[person]["bid"]
#         highest_bidder = auction_records[person]["name"]
#     print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
#   elif more_bidders == "yes":
#     clear()


# This solution uses Dictionaries only

def find_highest_bidder(bidding_record):
  highest_bid = 0
  highest_bidder = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      highest_bidder = bidder
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

bids = {}
auction_running = True

while auction_running:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bids[name] = bid
  
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  
  if more_bidders == "no":
    auction_running = False
    find_highest_bidder(bids)
  elif more_bidders == "yes":
    clear()