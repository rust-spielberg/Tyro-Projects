import random 

First were gonna' add statement "import random" which is a built-in module which helps you to genrate random number (either aas int or as float) in the range of [a,b]


def guess(x):
    rnd_num = random.randint(a,b)

Now we have defined a function called 'guess' with parameter x. We have random.randint(a,b) which allows comp to generate any random number N which is (a <= N <= b) and store it value in 'rnd_num'

Now to make our comp give us hints we gonna' need a loop with some if, elif statements

def guess(x):
    rnd_num = random.randint(a,b)
    num = 0
    while x != rnd_num :
        num = int(input("Guess the number between 1 to {x}))



num(100)
