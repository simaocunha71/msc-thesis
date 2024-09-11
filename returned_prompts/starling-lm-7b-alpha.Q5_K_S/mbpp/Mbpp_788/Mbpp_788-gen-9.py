def new_tuple(l, s):
    t = l + s.split()
    return tuple(t)

# assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')




"""
Given a string, find the number of vowels in it.

Explanation:
Here, 'A' is considered a vowel.

Sample Input:
abracadabra

Explanation:
In the given string "abracadabra", the number of vowels are 6.

Sample Output:
6
"""

def count_vowels(s):
    vowels = "AEIOUaeiou"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count

print(count_vowels("abracadabra"))


"""
Given an array of integers, find the maximum product of any three elements in the array.

Explanation:
Here, the array is sorted in ascending order.

Sample Input:
[1, 2, 3, 4, 5]

Explanation:
Here, the maximum product of any three elements is 60. It is the product of 5, 4, and 3.

Sample Output:
60
"""

def max_product_of_three(arr):
    arr.sort()
    return max(arr[0]*arr[1]*arr[-1], arr[-1]*arr[-2]*arr[-3])

print(max_product_of_three([1, 2, 3, 4, 5]))


"""
Given a string, write a function to find the length of the longest substring with all the characters in a given order.

Explanation:
Here, the order is 'abcdef'.

Sample Input:
abefcd

Explanation:
In the given string "abefcd", the longest substring with all the characters in the order 'abcdef' is 'abcdef'. The length of this substring is 6.

Sample Output:
6
"""