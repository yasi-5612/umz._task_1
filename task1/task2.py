account = {'bank': 0}

while True:
    print('What would you like to do?')
    print('Options: variz (deposit), bardasht (withdraw), etebar (credit)')
    action = input()

    if action == 'variz':
        print('Please enter the amount to deposit:')
        deposited_money = input()
        try:
            deposited_money = int(deposited_money)
        except ValueError:
            deposited_money = float(deposited_money)
        account['bank'] += deposited_money

    elif action == 'bardasht':
        print('Please enter the amount to withdraw:')
        withdraw_money = input()
        account['bank'] -= int(withdraw_money)

    elif action == 'etebar':
        print('Current balance:', account['bank'])

    else:
        print('Invalid action')