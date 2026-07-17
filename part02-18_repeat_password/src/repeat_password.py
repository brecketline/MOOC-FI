# Write your solution here
password = input('Password: ')
while True:
    repeated = input('Repeat password: ')

    if password == repeated:
        print('User account created!')
        break
    else:
        print('They do not match!')
