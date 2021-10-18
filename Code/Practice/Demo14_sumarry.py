# Program to find the sum of array

arr=[]

num=int(input("Enter the array number: "))
print(num)

for i in range(num):
	arry=int(input("Enter the numbers: "))
	arr.append(arry)
	print(arr)

ans = sum(arr)
#print("sum:", sum(arr))
print(ans)

'''
for a in len(List):
	sum=0
	sum = sum + arry[a]
	print(sum)	
'''
'''
#arr=[10,12,13,15]
ans = sum(arr)
#print("sum:", sum(arr))
print(ans)
'''

'''
##PROPER CODE#
#Python program to add all the array elements using the built-in function
lst = []
num = int(input("Enter the size of the array: "))
print("Enter array elements: ")
for n in range(num):
  numbers = int(input())
  lst.append(numbers)
print("Sum:", sum(lst))
'''