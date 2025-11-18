state = 'locked'

while True:
    while state == 'locked':
        state =input("Enter, coins, for coins, and push, to push forward.")
        if state == "push":
            print("Turnstile is locked")
            state = 'locked'
        elif state == 'coins':
            amount = int(input('Please enter 1 or more coins'))
            if amount >= 1:
                print('Turnstile is now unlocked, please proceed')
                state = 'unlocked'
            elif amount <1:
                amount = 0
                state = 'locked'      
    while state == 'unlocked':
        state = input("Enter, coins, for coins, and push, to push forward.")
        if state == "push":
            print("You have walked through")
            state = 'locked'
        elif state =="coins":
            state = input("Enter, coins, for coins, and push, to push forward.")
            state = 'unlocked'
