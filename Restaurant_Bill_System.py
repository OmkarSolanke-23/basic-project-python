
# customer = input("Enter customer name: ")


# # print("\n Restaurant Menu")
# # print("1. Pizza - 200")
# # print("2. Burger - 100")
# # print("3. Sandwich - ₹80")

# order = 0
# bill = 0
# total = 0
# for i in range(10):

#     food_name = input("Enter food name: ")
#     price = float(input("Enter  price: "))
#     quantity = int(input("Enter food quantity: "))

#     choice = int(input("Enter food choice (1-3): "))

#     if choice == 1:
#         item = "Pizza"
#         price = 200
#     elif choice == 2:
#         item = "Burger"
#         price = 100
#     elif choice == 3:
#         item = "Sandwich"
#         price = 80
#     else:
#         print("Invalid choice!")
#         continue

#     amount = price * quantity
#     total = total + amount

#     print("Item:", item)
#     print("Amount: ₹", amount)

# if total >= 500:
#     discount = total * 10 / 100
# else:
#     discount = 0

# final_bill = total - discount

# print("\n--- Restaurant Bill ---")
# print("Customer:", customer)
# print("Total Bill: ₹", total)
# print("Discount: ₹", discount)
# print("Final Bill: ₹", final_bill)
# print("Thank you!")


customer = input("Enter customer name: ")

total = 0

for i in range(3):
   

    
    food_name = input("Enter food name: ")
    price = float(input("Enter  price: "))
    quantity = int(input("Enter  quantity: "))
    

    amount = price * quantity
    total = total + amount

    print("Item:", quantity)
    print("Amount: ", amount)

if total >= 1000:
    discount = total * 10 / 100
elif total >= 500:
    discount = total * 5 / 100
else:
    discount = 0

gst = total *5 / 100 

final_bill = total - discount

print("\n Restaurant Bill ")
print("Customer:", customer)
print("Total Bill: ", total)
print("Discount: ", discount)
print("Final Bill: ", final_bill)
print("Thank you!")
