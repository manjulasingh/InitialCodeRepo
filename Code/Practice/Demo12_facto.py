# Program to find the factorial of a number
def fact(x):
	count = x
	if(count==1):
		return x
	else:
		x = x * fact(count-1)
		return x

	
num=int(input("Enter the number: "))
print(fact(num))		