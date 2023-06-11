import random

names = {}
number_of_user = input('Enter the number of friends joining (including you):\n')

# check if input is digit and greater than 0
if number_of_user.isdigit() and int(number_of_user) >= 1:
    number_of_user = int(number_of_user)

    # create list of names
    print('\nEnter the name of every friend (including you), each on a new line:')
    for i in range(number_of_user):
        name = input()
        names[name] = 0

    print('\nEnter the total bill value:')
    bill = float(input())
    if bill > 0:
        print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
        lucky = input()
        if lucky == 'Yes':
            lucky_name = random.choice(list(names.keys()))
            print(f'\n{lucky_name} is the lucky one!')
            split_bill = round(bill / (len(names) - 1), 2)
            for name in names:
                if name == lucky_name:
                    names[name] = 0
                else:
                    names[name] = split_bill
            print(names)
        elif lucky == 'No':
            print('\nNo one is going to be lucky')
            split_bill = round(bill / len(names), 2)
            for name in names:
                names[name] = split_bill
            print(names)
        else:
            print('\nInvalid input')
    else:
        print('\nInvalid input')
else:
    print('\nNo one is joining for the party')
