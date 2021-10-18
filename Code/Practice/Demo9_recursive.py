#python program to find the power of two number using recursion

def rec(num,y):
	count = y
	if(count==1):
		return num
	else:
		num = num * rec(num,count-1)
		return num
		

num1=int(input("please enter the number: "))
#print(num)
num2=int(input("please enter the number: "))
#print(y)
print(rec(num1,num2))