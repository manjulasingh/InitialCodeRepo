# Program to find the simple interest
def simint(p,r,t):
	si = (p*r*t)/100
	return si 


num1=int(input("Enter the value of P: "))
num2=int(input("Enter the value of R: "))
num3=int(input("Enter the value of T: "))

print(num1,num2,num3)

print(simint(num1,num2,num3))	