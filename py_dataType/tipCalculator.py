print("Welcom to the top calculatr.");
bill = input("What was the total bill?\n$");
tipPercentage = input("What percentage tip would you like to give?\n10, 12, or 15?");
people = input("How many people to split the bill?\n");

tip = int(tipPercentage) / 100;
tipBill = float(bill) * tip;
totalBill = float(bill) + tipBill
# splitBill = round(totalBill / int(people),2);
splitBill = "{:.2f}".format(round(totalBill / int(people),2));
print(f"Each person should pay: ${splitBill}");
