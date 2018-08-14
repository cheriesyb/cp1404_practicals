
"""def shop_calculator():
    total_price = 0
    number_of_items = int(input("Number of items: "))
    validate_input(number_of_items)
    for i in range(number_of_items):
        price_of_item = float(input("Price of item: "))
        total_price += price_of_item
    print("Total price for", number_of_items, "items  is " + "$" + str(total_price))

def validate_input(number_of_items):
    while not number_of_items > 0:
        print(input("Please enter the number of items: "))

shop_calculator()"""

total = 0
number = int(input("Enter the number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Enter the number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total *= 0.9

print("Total price for ", number, " items is $", total, sep="")