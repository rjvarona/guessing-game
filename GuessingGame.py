import random
value = int(input("Guess a value from 1 to 100:"))
x = random.randint(1,101)
if value > x:
	print("The number is too high")
elif value < x:
        print ("The number is too low")
elif value == x:
	print("you got it fam")
while value != x:
	value = int(input("Guess a value from 1 to 100:"))
	if value > x:
		print("The number is too high")
	elif value < x:
		print ("The number is too low")
	elif value == x:
		print("you got it fam")

