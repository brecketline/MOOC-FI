# Write your solution here
amount_tax = 0
value_gift = int(input('Value of gift: '))
if value_gift < 5000:
    amount_tax = 0
elif value_gift < 25000:
    amount_tax = (100 + (value_gift - 5000) * 0.08)
elif value_gift < 55000:
    amount_tax = (1700 + (value_gift - 25000) * 0.10)
elif value_gift < 200000:
    amount_tax = (4700 + (value_gift - 55000) * 0.12)
elif value_gift < 1000000:
    amount_tax = (22100 + (value_gift - 200000) * 0.15)
elif value_gift >= 1000000:
    amount_tax = (142100 + (value_gift - 1000000) * 0.17)

if amount_tax == 0:
    print('No tax!')
else:
    print(f'Amount of tax: {amount_tax} euros')
