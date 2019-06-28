import random

goal = random.choice('ACGT')
for i in range(4):
    goal += random.choice('ACGT')

guess = 'NNNNN'

name = input('Player what is your name?')


while guess != goal:
    guess = input('Guess a 5 bp primer: ')
    while len(guess) != 5:
        guess = input('Please, guess a 5 bp primer: ')
    a=0
    misses = 0
    for i in range(len(guess)):
        if guess[i] != goal[i]:
            a=i+1
            misses += 1
            if misses > 0:
                print('Sorry, base number %i is wrong. ' %a )
                if i==4:
                    print('You guess %s bases wrong. Play again?' %misses)

print('Excellent work %s, you won!' % name)

