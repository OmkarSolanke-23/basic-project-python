customer_name = input("Enter customer name: ")
num_products = int(input("Enter number of products: "))

total_bill = 0

for i in range(1, num_products + 1):
    print(f"\nProduct {i}")

    product_name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    product_total = price * quantity
    total_bill += product_total

    print(f"Product Name: {product_name}")
    print(f"Product Total: ₹{product_total:.2f}")

print("\nSHOPPING BILL ")
print(f"Customer Name: {customer_name}")
print(f"Total Bill Before Discount: ₹{total_bill:.2f}")

if total_bill >= 5000:
    discount = total_bill * 0.10
elif total_bill >= 3000:
    discount = total_bill * 0.05
else:
    discount = 0

final_bill = total_bill - discount

print(f"Discount: ₹{discount:.2f}")
print(f"Bill After Discount: ₹{final_bill:.2f}")

if final_bill >= 5000:
    final_bill -= 200
    print("Additional Discount: ₹200")

print(f"Final Amount to Pay: ₹{final_bill:.2f}")
print("Final Bills")


    




