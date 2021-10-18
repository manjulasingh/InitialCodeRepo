## To take the input from user to create a list and append the list one by one##

List=[]

val=input("Enter the number of data in list:")
print(val)

for num in range(int(val)):
	value=input("Please enter the number in List: ")
	print(value)
	List.append(value)
print("the new List is :",List)

'''
## To check and print the value from the list if its greater than 25 or less than##
List=[10,20,15,40,25]

for x in range(len(List)):
	if List[x]>=25:
		print("List is greater")
		
		print(List[x])
	else:
		print("List is smaller")
		print(List[x])
		'''