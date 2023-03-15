import random
print('Created By Daniel C. Opute')
print('Hello! welcome to Guess and Win')
print('Instruction: This is a guessing game, and based on your choice you stand a chance of winning 3 Prices')
print("Use Y for 'Yes' and N for 'No' when asked a question")
print('PRICES 1: N500K')
print('PRICE 2: N300K')
print('PRICE 3: N400K')

# If total = 20 win price 1
# If total = 15 win price 2
# if total = 10 win price 3

def begin():
    start = input('Are you ready? Yes(Y)/No(N): ').capitalize()

    def new_game():
        if start == 'Y':
            name = input("What's your name?: ").title()
            print(f"Hello, {name} Welcome to Guess Me! Here your choice matters alot. ")
            print('Answer the following question to stand a chance of winning')

            def choice_one():
                question_one = int(input('Pick a number from One to Three (1, 2, 3, 4 or 5): '))
                global ran_num_1
                global num_1
                ran_num_1 = 0
                num_1 = 0
                if question_one <= 3:
                    ran_num_1 = random.randint(0, 5)
                elif question_one > 3 <= 5:
                    num_1 = 5
                else:
                    print('Invalid response: Try again')
                    choice_one()

            choice_one()

            def choice_two():
                question_two = input('do you like Football? Yes(Y)/No(N): ').capitalize()
                global ran_num_2
                global num_2
                ran_num_2 = 0
                num_2 = 0
                if question_two == 'Y':
                    ran_num_2 = random.randint(0, 5)
                elif question_two == 'N':
                    num_2 = 5
                else:
                    print('Invalid response: Try again')
                    choice_two()

            choice_two()

            def choice_three():
                question_three = input('Do you love Nigeria? Yes(Y)/No(N): ').capitalize()
                global ran_num_3
                global num_3
                ran_num_3 = 0
                num_3 = 0
                if question_three == 'N':
                    ran_num_3 = random.randint(0, 5)
                elif question_three == 'Y':
                    num_3 = 5
                else:
                    print('Invalid response: Try again')
                    choice_three()

            choice_three()

            def choice_four():
                question_four = input('Would you choose another country above nigeria '
                                      'if you had the chance? Yes(Y)/No(N): ').capitalize()
                global ran_num_4
                global num_4
                ran_num_4 = 0
                num_4 = 0
                if question_four == 'Y':
                    ran_num_4 = random.randint(0, 5)
                elif question_four == 'N':
                    num_4 = 5
                else:
                    print('Invalid response: Try again')
                    choice_four()

            choice_four()

            # Calculate Score
            def evaluate_result():
                price_one = 20
                price_two = 15
                price_three = 10

                price_1 = '500K'
                price_2 = '300K'
                price_3 = '100K'

                def claim():
                    receive = input('Claim your reward, Yes(Y)/No(N)').capitalize()
                    if receive == 'Y':
                        account = int(input('Enter Your Account Number: '))
                        print('Thanks for playing')
                    elif receive == 'N':

                        def reward_lost():
                            lose_reward = input('Sorry, You Just Lose Your Reward: '
                                                'Play Again Yes(Y)/No(N)').capitalize()
                            if lose_reward == 'Y':
                                begin()
                            elif lose_reward == 'N':
                                print('Bye, Nice having you visit. Hope to see you next time.')
                            else:
                                print('Invalid response: Try again')
                                reward_lost()
                        reward_lost()
                    else:
                        print('Invalid response: Try again')
                        claim()

                total = ran_num_1 + num_1 + ran_num_2 + num_2 + ran_num_3 + num_3 + ran_num_4 + num_4
                if total == price_one:
                    print('Congratulations! You WON! 1st Position.')
                    print(f'You Reward is {price_1}')
                    claim()
                elif total == price_two:
                    print('Congratulations! You WON! 2st Position.')
                    print(f'You Reward is {price_2}')
                    claim()
                elif total == price_three:
                    print('Congratulations! You WON! 3st Position.')
                    print(f'You Reward is {price_3}')
                    claim()
                elif total < 10:
                    def poor_choice():
                        poor = input('Your Choices were too poor: Try again Yes(Y)/No(N)').capitalize()
                        if poor == 'Y':
                            begin()
                        elif poor == 'N':
                            print('Thank you for playing. Hope to see you next time')
                        else:
                            print('Invalid Response:')
                            poor_choice()

                    poor_choice()
                elif total > 20:
                    def high_choice():
                        high = input('Your Choice were too high: Try again Yes(Y)/No(N)').capitalize()
                        if high == 'Y':
                            begin()
                        elif high == 'N':
                            print('Thank you for playing. Hope to see you next time')
                        else:
                            print('Invalid Response:')
                            high_choice()

                    high_choice()
                else:
                    def close_choice():
                        close = input('You were so close: Try again Yes(Y)/No(N)').capitalize()
                        if close == 'Y':
                            begin()
                        elif close == 'N':
                            print('Thank you for playing. Hope to see you next time')
                        else:
                            print('Invalid Response:')
                            close_choice()

                    close_choice()

            evaluate_result()
        elif start == 'N':
            print('Thanks for visiting. Hope to see you next time.')
        else:
            print('Invalid Entry: Try again')
            begin()

    new_game()


begin()
