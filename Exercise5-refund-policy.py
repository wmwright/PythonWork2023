days_since_purchase = int(input("How many days ago have you purchased the item? "))
used_item = input("Have you used the item at all [y/n]? ").lower()
broken_down = input("Has the item broken down on its own [y/n]? ").lower()

if (days_since_purchase <= 10 and used_item == 'n') or broken_down == 'y':
    print("You can get a refund.")
else:
    print("You cannot get a refund.")
