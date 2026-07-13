# Write your solution here
hourly_wage = float(input('Hourly wage: '))
hours_worked = int(input('Hours worked: '))
day_week = input('Day of the week: ')
if day_week != 'Sunday':
    daily_wages = hourly_wage * hours_worked
else:
    daily_wages = (hourly_wage * 2) * hours_worked

print(f'Daily wages: {daily_wages} euros')
