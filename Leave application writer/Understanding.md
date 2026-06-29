String concatenation(aka putting strings together)
suppose want to create a string "subscribe to _______"
and in the place of _________ We want some youtubers name
for ex.
"Rider Op"
so creating a variable string 
youtuber = "Rider Op" #variabla string

now to print "subscribe to Rider Op"

we can have a few ways :

1 String concatenation
print("Subscribe to " + youtuber ) #basic string concatenation
  

2 .format() method
print("Subscribe to {}".format(youtuber))
#In this {} is a blank space which will be filled by the value of youtuber wtv it is by using (.format(youtuber))

3 f-string method
print(f"subscribe to {youtuber}")
the f in this tells python:
anything inside {} is python code. evaluate it and then run it



the whole program is written in f-string method ..... and Also given user the choice
by adding
print("1. School Student")
print("2. College Student")
print("3. Working Individual")

choice = input("Enter your choice (1/2/3): ")
with if,elif,else conditions 
so user can choose wtv he needs
