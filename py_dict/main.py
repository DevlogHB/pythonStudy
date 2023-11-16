import os
from art import logo
# os.system("cls")

print(logo);

# dict 생성
bids = {};
finished = False;

# 경매 가격 체크(가격이 높은사람 찾기) 
def find_highest_bidder(bidding_recode):
    highest_bid = 0;
    winner = "";
    for bidder in bidding_recode:
       if highest_bid < bidding_recode[bidder]:
            highest_bid = bidding_recode[bidder];
            winner = bidder;
    print(f"The winner is {winner} with a bid of ${highest_bid}");

while not finished:
    name = input("What is your name?");
    price = int(input("What is your bid? $"));
    bids[name] = price;
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'.");
    if should_continue.lower() == "no":
        finished = True;
        find_highest_bidder(bids);
    elif should_continue.lower() == "yes":
        os.system("cls"); # clear 처리


