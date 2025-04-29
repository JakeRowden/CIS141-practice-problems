#Asks users for the order total and prints the total cost, including shipping. Store charges $5 for shipping on any order under $50. If the order is more than $50 shipping is free.

order_cost = float(input("What was the cost of your order?"))

if order_cost< 50:
    order_cost = order_cost + 5
    print("Your order with shipping will cost $" + str(order_cost))
else:
    print("Your order will cost $" + str(order_cost) + ". Shipping is free.")
