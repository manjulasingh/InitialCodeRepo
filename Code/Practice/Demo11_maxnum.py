# program to find the maximum number from two numbers


def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b

num1=input("enter the first num:")
num2=input("enter the second num:")
print(maximum(num1,num2))

#list[]=list.append(num1,num2)
'''
if(num1>=num2):
	print("{0} is greater than {1}".format(num1,num2))
else:
	print("{1} is greater than {0}".format(num2,num1))
	'''