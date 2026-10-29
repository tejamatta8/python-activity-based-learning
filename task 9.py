rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

if rows <= 0 or columns <= 0:
    print("Invalid classroom dimensions")
else:
    seat = 1

    for i in range(rows):
        for j in range(columns):
            print("S" + str(seat), end="\t")
            seat += 1

        print()
