def pair_xor_Sum(lst: list, n: int) -> int:
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += lst[i] ^ lst[j]
    return sum * 2

print(pair_xor_Sum([5,9,7,6],4)) # 47

Explanation:
We need to find the sum of XOR of all pairs of numbers in the given list. 
The XOR of two numbers is a bitwise operator that compares each bit of two integers and gives 1 if the bits are different, else it gives 0.
The logic to solve this problem is to find all possible pairs of numbers in the list and calculate their XOR. Sum them up and return the result.
The inner loop starts from i+1 because we need to get unique pairs. The outer loop runs till n-1 because we are considering n elements in the list and we are not considering the last element in the list in the inner loop.
The return statement multiplies the sum by 2 because in the question it is mentioned that for each pair we count the pair (a,b) and (b,a), so there are 2 counts.
"""


"""
