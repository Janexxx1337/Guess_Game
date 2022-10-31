import random

logo = '''   .------..------..------..------..------..------.     .------..------..------.     .------..------..------..------.
|C.--. ||H.--. ||O.--. ||O.--. ||S.--. ||E.--. |.-.  |N.--. ||U.--. ||M.--. |.-.  |G.--. ||A.--. ||M.--. ||E.--. |
| :/\: || :/\: || :/\: || :/\: || :/\: || (\/) ((5)) | :(): || (\/) || (\/) ((5)) | :/\: || (\/) || (\/) || (\/) |
| :\/: || (__) || :\/: || :\/: || :\/: || :\/: |'-.-.| ()() || :\/: || :\/: |'-.-.| :\/: || :\/: || :\/: || :\/: |
| '--'C|| '--'H|| '--'O|| '--'O|| '--'S|| '--'E| ((1)) '--'N|| '--'U|| '--'M| ((1)) '--'G|| '--'A|| '--'M|| '--'E|
`------'`------'`------'`------'`------'`------'  '-'`------'`------'`------'  '-'`------'`------'`------'`------'
                                                                                                       '''
arr = list(range(1, 100))


def helloThere():
    print(logo)
    print("Welcome to 'Number Guessing Game'!")
    print('Am thinking of a number between 1 and 100')


helloThere()


def difficult():
    random_number = int(random.choice(arr))
    print(random_number)
    easy_attempts = 10
    hard_attempts = 5
    choose_dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose_dif == 'easy':
        print(f'Alright! You have {easy_attempts} remaining to guess number')
        while easy_attempts > 0:
            guess = int(input('Make a guess : '))

            if random_number == guess:
                print('Congratulation! You are the winner!')

            elif random_number < guess:
                easy_attempts -= 1
                print(f'Its to high!\n You have {easy_attempts} attempts to remaining!')

            elif random_number > guess:
                easy_attempts -= 1
                print(f'Its to low!\n You have {easy_attempts} attempts to  remaining!')

    else:
        print(f'Alright! You have {hard_attempts} remaining to guess number')

        while hard_attempts > 0:
            guess = int(input('Make a guess : '))

            if random_number == guess:
                print('Congratulation! You are the winner!')

            elif random_number < guess:
                hard_attempts -= 1
                print(f'Its to high!\n You have {hard_attempts} attempts to  remaining!')

            elif random_number > guess:
                hard_attempts -= 1
                print(f'Its to low!\n You have {hard_attempts} attempts to  remaining!')


difficult()
