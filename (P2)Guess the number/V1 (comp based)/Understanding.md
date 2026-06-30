import random 

First were gonna' add statement "import random" which is a built-in module which helps you to genrate random number (either aas int or as float) in the range of [a,b]


def guess(x):
    rnd_num = random.randint(a,b)

Now we have defined a function called 'guess' with parameter x. We have random.randint(a,b) which allows comp to generate any random number N which is (a <= N <= b) and store it value in 'rnd_num'

Now to make our comp give us hints we gonna' need a loop with some if, elif statements

def guess(x):
    rnd_num = random.randint(a,b)
    num = 0
    while num != rnd_num:
        num = int(input(f"Guess the number b/w 1 to {x}: "))
        diff = abs(rnd_num - num)
        if num < rnd_num :


num(100)

here we defined a variable named "num" which has initial starting value of 0 ... after that we have a loop which will stops when the num = rnd_num
I've also given it some conditions to give user hint about the number he selected is way too far or is close to the original number 


import pyfiglet
print(pyfiglet.figlet_format("Congratulations!!"))

we first installed this lib for great font visual ..... so when the user gets the correct number it prints congratulations in a special style

