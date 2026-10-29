basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
overtime = float(input("Enter overtime amount: "))

gross = basic + allowance + overtime
deduction = gross * 0.10
net_salary = gross - deduction

print("Basic Salary:", basic)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net_salary)
