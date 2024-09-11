"""
def find_Odd_Pair(arr,num):
    c=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]^arr[j])&1:
                c+=1
    return c
"""

def find_Odd_Pair(arr,num):
    c=0
    for i in range(len(arr)):
        if (num^arr[i])&1:
            c+=1
    return c

find_Odd_Pair([5,4,7,2,1],5)
#find_Odd_Pair([1,2,3,4,5],3)
#find_Odd_Pair([1,2,3,4,6],3)
#find_Odd_Pair([1,2,3,4,7],3)
#find_Odd_Pair([1,2,3,4,8],3)

"""
Explanation:
This problem can be solved by using a python function to count the number of pairs whose xor value is odd. The function finds the number of pairs whose xor value is odd by iterating through the array and checking if the xor value of each pair is odd. The function returns the total count of such pairs.
"""

"""
Explanation:
This problem can be solved by using a python function to count the number of pairs whose xor value is odd. The function finds the number of pairs whose xor value is odd by iterating through the array and checking if the xor value of each pair is odd. The function returns the total count of such pairs.
"""

# Python program to print prime factors of a number

def primeFactors(n):
    # Print the number of 2s that divide n
    while n % 2 == 0:
        print 2,
        n = n / 2

    # n must be odd at this point. So we can skip one element
    # (Note i = i +2)
    for i in range(3,int(n**0.5)+1,2):

        # While i divides n, print i and divide n
        while n % i