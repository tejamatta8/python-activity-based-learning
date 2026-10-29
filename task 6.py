attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
else:
    percentage = (attended / total) * 100

    print("Current Attendance:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Attendance requirement satisfied")
    else:
        extra = 0

        while (attended + extra) / (total + extra) < 0.75:
            extra += 1

        print("Additional classes required:", extra)
