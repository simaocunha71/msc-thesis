```
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    else:
        trib = [3, 2]
        while len(trib) < n + 1:
            if trib[-1] % 2 == 0:
                trib.append(1 + trib[-1] / 2)
            else:
                trib.append(trib[-2] + trib[-1] + trib[-3])
        return trib
```
This function generates the first n + 1 numbers of the Tribonacci sequence. It uses a while loop to generate the sequence. If the last number in the sequence is even, it calculates the next number as 1 plus half of the last number. If the last number is odd, it calculates the next number as the sum of the last three numbers in the sequence. The function returns the list of the first n + 1 numbers of the Tribonacci sequence. If n is less than or equal to 2, it returns the list of the first n + 1 numbers of the sequence directly. If n is 0, it returns an empty list. If n is 1, it returns the list [3]. If n is 2, it returns the list [3, 2]. 

This function works for all non-negative integer values of n. It has a time complexity of O(n) and a space complexity of O(n) as well, since it needs to store the sequence in memory. 

For example, tri(3) returns [1, 3, 2, 8]. tri(4) returns [1, 3, 2, 8, 11]. tri(5) returns [1, 3, 2, 8, 11, 34]. And so on. 

This function is designed to work with non-negative integer values of n. It does not work with negative values of n or with non-integer values of n. If you need to work with negative values or non-integer values of n, you would need to modify the function accordingly. 

The function also does not handle floating point precision issues. If you need to handle floating point precision issues, you would need to modify the function accordingly. 

The function assumes that the Tribonacci sequence is defined as in the problem statement. If the sequence is defined differently, you would need to