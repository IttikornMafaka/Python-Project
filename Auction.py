print('''         
         ____
       __/____\___
      |___________|
           ||
     _____ || _____
    |      ||      |
    |   AUCTION    |
    |______________|
''')
print("Welcome to the Auction Center")

# collect Data
data_bid = {}

def compare_cost(data_bid):
    winner = ""
    highest_bid = 0
    for bidder in data_bid:
        bid_amount = data_bid[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

# start competition
continue_bid = True
while continue_bid:
    name = input("What is your name: ")
    cost = int(input("What is your bid: "))
    data_bid[name] = cost

    should_con = input("Has anyone else want to bid more? yes/no: ").lower()
    if should_con == "no":
        continue_bid = False
        compare_cost(data_bid)
    elif should_con == "yes":
        print("\n" * 20)
