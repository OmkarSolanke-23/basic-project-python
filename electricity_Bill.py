name = input("Enter customer name: ")
units = int(input("Enter electricity units: "))
bill = 0
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10


surcharger = 0
penalty = 0
if bill >= 2000 :
    surcharger  = bill *5 / 100
if units > 300:
    penalty = 150

total_bill = bill + surcharger + penalty
print("\nElectricity Bill")
print("Customer Name:", name)
print("Units Consumed:", units)
print("Total Bill: ", total_bill)