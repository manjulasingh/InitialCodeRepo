list = [ '20', '30', '40']
print(list)	

'''
user_in1 = input('Please enter first number: ')
print(user_in1)

user_in2 = input('Please enter second number: ')
print(user_in2)

user_in3 = input('Please enter third number: ')
print(user_in3)

print(user_in1,user_in2,user_in3)
'''

#new_list=len(list)
for item in range(len(list)):
	user_in1 = input('Please enter number: ')
	print(user_in1)

	list[item] = user_in1
print(list)

for item in range(len(list),10,1):
	user_in2 = input('Please enter number: ')
	print(user_in2)

	list.append(user_in2)
print(list)
