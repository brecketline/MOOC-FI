# Write your solution here
year = int(input('Year: '))
year_test = year + 1

while not ((year_test % 4 == 0 and year_test % 100 != 0) or (year_test % 400 == 0)):
    year_test += 1
print(f'The next leap year after {year} is {year_test}')
