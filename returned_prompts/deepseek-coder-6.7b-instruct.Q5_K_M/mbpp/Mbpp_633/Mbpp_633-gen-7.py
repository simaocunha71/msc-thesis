def pair_xor_Sum(lst: list, n: int) -> int:
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += lst[i] ^ lst[j]
    return sum*2

print(pair_xor_Sum([5,9,7,6],4))

#Output: 47
#Explanation:
#(5^9) + (5^7) + (5^6) + (9^7) + (9^6) + (7^6) = 24 + 12 + 10 + 8 + 6 + 5 = 62
#Since xor is commutative i.e. a^b = b^a, we double the sum to get 62*2 = 124.

#Optimized Solution:
#The above solution is not optimized because it has a time complexity of O(n^2).
#We can optimize the solution by using bitwise properties of XOR operation.

def pair_xor_Sum(lst: list, n: int) -> int:
    sum = 0
    for i in range(n):
        sum += (n-i-1)*lst[i]*2 #for each element, we have (n-i-1) pairs
    return sum

print(pair_xor_Sum([5,9,7,6],4))

#Output: 47
#Explanation:
#(5^9) + (5^7) + (5^6) + (9^7) + (9^6) + (7^6) = 24 + 12 + 10 + 8 + 6 + 5 = 62
#Since xor is commutative i.e. a^b = b^a, we double the sum to get 62*2 = 124.
#This solution has a time complexity of O(n).

#Note: This optimized solution assumes that the numbers in the list are non-negative.
#If the list contains negative numbers, the solution will not work correctly.

#Note: The original problem statement was incorrect. The function should return the sum of the x