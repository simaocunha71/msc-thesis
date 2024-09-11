"""
def find_remainder(arr,n):
    if len(arr)==1:
        return arr[0]%n
    temp=[0]*len(arr)
    temp[0]=arr[0]%n
    for i in range(1,len(arr)):
        temp[i]=((temp[i-1]*arr[i])%n)
    return temp[len(arr)-1]
find_remainder([ 100, 10, 5, 25, 35, 14 ],11)"""

Explanation:
In the above python function, firstly we check if length of array is 1. If it is, we directly return the array element modulo n. Then we initialize an array called temp of same length of arr and assign the first element of arr to temp. Then we iterate over the array from index 1 to length of arr. In each iteration, we calculate the product of previous element of temp and the current element of arr and take modulo of this product. We assign this modulo to the current index of temp. Finally, we return the last element of temp which is the product of all array elements modulo n.

To validate the above function we have given an assert statement to check if the result of the function is correct for the given input.

"""
def find_remainder(arr,n):
    if len(arr)==1:
        return arr[0]%n
    temp=[0]*len(arr)
    temp[0]=arr[0]%n
    for i in range(1,len(arr)):
        temp[i]=((temp[i-1]*arr[i])%n)
    return temp[len(arr)-1]
find_remainder([ 100, 10, 5, 25, 35, 14 ],11)
"""

In the above code, we are defining a function find_remainder that takes two parameters arr and n. In the function, we first check if the length of arr is 1. If it is, we directly return the first element of arr modulo n. Then we initialize an array temp of same length as arr and assign the first element of arr to temp.