


name = input("Enter customer name: ")
weight = float(input("Enter package weight in kg: "))
distance = float(input("Enter delivery distance in km: "))

choice = input("Enter delivery type (standard/express): ")

base_charge = 50
weight_charge = 0
distance_charge = 0
express_charge = 0
discount = 0

if weight > 5:
    weight_charge = (weight - 5) * 20

if distance > 50:
    distance_charge = 100

total = base_charge + weight_charge + distance_charge

if choice.lower() == "express":
    express_charge = total * 0.50

total = total + express_charge

if total > 300:
    discount = total * 0.10

final_charge = total - discount

print("\n--- Delivery Details ---")
print("Customer Name:", name)
print("Package Weight:", weight, "kg")
print("Delivery Distance:", distance, "km")
print("Base Charge: Rs.", base_charge)
print("Weight Charge: Rs.", weight_charge)
print("Distance Charge: Rs.", distance_charge)
print("Express Charge: Rs.", express_charge)
print("Discount: Rs.", discount)
print("Final Delivery Charge: Rs.", final_charge)