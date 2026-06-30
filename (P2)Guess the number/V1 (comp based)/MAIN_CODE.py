import random
import pyfiglet


def guess(x):
    rnd_num = random.randint(1,x)
    num = 0
    while num != rnd_num:
        num = int(input(f"Guess the number b/w 1 to {x}: "))
        diff = abs(rnd_num - num)
        if num < rnd_num :
            if 5 < diff < 10:
                print("Try again .... Sill low")
            elif diff <= 5 :
                print("Just gonna get it....")
            elif diff > 10 :
                print("Never gonna' get it.... Way too low")

            
        elif num > rnd_num :
            if 5 < diff < 10:
                print("Try again .... Sill high!!")
            elif diff <= 5 :
                print("Just gonna get it....")
            elif diff > 10 :
                print("Never gonna' get it.... Way too High!!!!")
        else:
            print(pyfiglet.figlet_format("Congratulations!!"))



guess(50)