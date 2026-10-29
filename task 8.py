mark1 = float(input("Enter first exam marks: "))
mark2 = float(input("Enter second exam marks: "))
mark3 = float(input("Enter third exam marks: "))

average = (mark1 + mark2 + mark3) / 3

print("Average Marks:", round(average, 2))

if mark1 < mark2 < mark3:
    print("Performance is improving")
elif mark1 > mark2 > mark3:
    print("Performance is declining")
else:
    print("Performance is fluctuating")

if average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")
