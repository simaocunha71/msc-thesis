
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)

# Example:

print(solution([5, 8, 7, 1])) #==> 12
print(solution([3, 3, 3, 3, 3])) #==> 9
print(solution([30, 13, 24, 321])) #==>0

# Explaination:

In the first example, the odd elements in even positions are 5 (at position 0) and 7 (at position 2). Their sum is 12.
In the second example, all elements are odd and they are in even positions, so their sum is 9.
In the third example, there is no odd element in even position, so the sum is 0.




# Solution 2:

