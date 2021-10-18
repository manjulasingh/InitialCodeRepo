#Program for array rotation
'''
# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
 
 
# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))
'''
'''
# slicing approach to rotate the array
def rotateList(arr,d,n):
  arr[:]=arr[d:n]+arr[0:d]
  return arr
  
# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6]
print(arr)
print("Rotated list is")
print(rotateList(arr,2,len(arr))) 
'''

list1=['1','2','3','4','5','6','7'] 

arr=[]
n=len(list1)
#print(n)
for i in range(n):
    var=list1[i-5]
    #print(var)
    arr.append(var)
print(arr)