# Program to print prime number
var=0
num=int(input("Enter the number: "))
print(num)
if num > 1:
	for i in range(2,num//2):
		if num%i == 0:
			var = 1
			break
			#print("not prime")

	if var == 1:
		print("number is not prime")
	else:
		print("number is prime")

	'''
	23
	rane(2,11)
	23%2=1
	23%3=2
	23%4=3
	

	'''	
				

