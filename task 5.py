venue = float(input("Enter venue cost: "))
food = float(input("Enter food cost: "))
equipment = float(input("Enter equipment cost: "))
participants = int(input("Enter number of participants: "))

total_cost = venue + food + equipment

if participants > 0:
    contribution = total_cost / participants

    print("Total Event Cost:", total_cost)
    print("Contribution per Participant:", round(contribution, 2))
else:
    print("Number of participants must be greater than zero")
