import random
def throw():
    throw={1:'Rock',2:'Paper',3:'Scissors'}
    index=(1,2,3)
    choice=random.choice(index)
    return throw[choice]
def option_checker():
    try:
        option=int(input('Enter 1:Rock 2:Paper 3:Scissors 4:Exit: '))
        if option<5 and option>0:
            throw={1:'Rock',2:'Paper',3:'Scissors',4:'exit'}
            return throw[option] 
        else:
            return 'Enter a Valid Option'
    except ValueError:
        return 'Enter a Valid Option'
def logic(user_option,cpu_option):
    if user_option==cpu_option:
        return"It's a Tie!"
    elif (user_option=='Rock' and cpu_option=='Paper') or (user_option=='Paper' and cpu_option=='Scissors')or (user_option=='Scissors' and cpu_option=='Rock'):
        return'You Lose!'
    else:
        return'You Win!'

def counter(result,user_score,cpu_score):
    if result=='You Win!':
        user_score+=1
    elif result=='You Lose!':
        cpu_score+=1
    elif result=="It's a Tie!":
        pass
    else:
        pass
    return user_score,cpu_score
#GLOBAL STUFF   
user_score,cpu_score,round_count=0,0,1
while True:
    try:
        rounds=int(input('Enter the number of rounds:'))
        break
    except ValueError:
        print('Enter a Valid Option')
for i in range(rounds):
    print(f'ROUND:{round_count}')
    user_option=option_checker()
    if user_option=='exit':
        break
    elif user_option=='Enter a Valid Option':
        print(f'\n{user_option}\n')
        continue
    else:
        round_count+=1
        cpu_option=throw()
        print(f'\nYour Option: {user_option}')
        print(f'CPU option: {cpu_option}')
        win_or_lose=logic(user_option,cpu_option)
        print(win_or_lose)
        user_score,cpu_score=counter(win_or_lose,user_score,cpu_score)
        print(f'YOU:{user_score} CPU:{cpu_score}\n')
else:
    if user_score>cpu_score:
        print('\n YOU WIN THE GAME!')
    elif user_score<cpu_score:
        print('\n YOU LOSE THE GAME!')
    else:
        print('\n IT IS A TIE!')


