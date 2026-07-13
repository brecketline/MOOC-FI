# Write your solution here
cafeteria_times = int(
    input('How many times a week do you eat at the student cafeteria? '))
price = float(input('The price of a typical student lunch? '))
weekly_groceries = float(
    input('How much money do you spend on groceries in a week? '))

daily = (((price * cafeteria_times) / 7) + (weekly_groceries / 7))
weekly = daily * 7

print('Average food expenditure: ')
print(f'Daily: {daily} euros')
print(f'Weekly: {weekly} euros')
