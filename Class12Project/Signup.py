from Helper import get_data_from_table, execute_sql, add_delay

users = get_data_from_table('select * from user_list')
usernames = users.username.values


def welcome():
    print('-' * 70)
    print('REGISTRATION PORTAL'.center(70, '-'))
    print('-' * 70)
    register()


def register(rank='CUSTOMER'):

    print('Enter your username: ', end='')
    username = usernames[0]
    while (username := input()) in usernames:
        print('This username already exists. Please enter a new username')

    password = input('Enter your password: ')
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    execute_sql(
        f'insert into user_list values("{firstname}", "{lastname}", "{username}", "{password}", " ", "{rank}")')

    print('Account created successfully. Heading back to login portal... ')
    import Login
    add_delay()
    Login.welcome()

