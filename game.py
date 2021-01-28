# Write your code here
import random
import sys
options = ['sciccors', 'paper', 'rock']
choice = input()
if choice not in options:
    sys.exit()
cpu_choice = random.choice(options)
ch = options.index(choice)
cpu = options.index(cpu_choice)
if choice == cpu_choice:
    print(f'There is a draw ({cpu_choice})')
elif ch == cpu + 1 or cpu + 2 == ch:
    print(f'Well done. The computer chose{cpu_choice} and failed')
elif cpu == ch + 1 or ch + 2 == ch:
    print(f'Sorry, but the computer chose {cpu_choice}')
