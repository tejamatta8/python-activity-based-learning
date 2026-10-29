price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 2000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("Total Amount:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
