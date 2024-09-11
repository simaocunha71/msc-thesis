def armstrong_number(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**len(str(n))
        temp//=10
    if sum==n:
        return True
    else:
        return False



"""
Given an array of numbers, return the number of even and odd integers in the array
"""

def count_even_odd(arr):
    count_odd=0
    count_even=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            count_even+=1
        else:
            count_odd+=1
    return count_odd,count_even

"""
Write a function that returns the index of the first occurrence of an element in a given array
"""

def first_occurrence(arr, element):
    for i in range(len(arr)):
        if arr[i]==element:
            return i
    return -1

"""
Write a function that returns the index of the last occurrence of an element in a given array
"""

def last_occurrence(arr, element):
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==element:
            return i
    return -1

"""
Write a function that returns the maximum and minimum value in a given array
"""

def min_max(arr):
    max_num=arr[0]
    min_num=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_num:
            max_num=arr[i]
        if arr[i]<min_num:
            min_num=arr[i]
    return max_num,min_num

"""
Write a function that returns the sum of all elements in a given array
"""

def sum_array(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    return sum

"""
Write a function that returns the product of all elements in a given array
"""
def product_array