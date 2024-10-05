    result = 0
    for i, element in enumerate(lst):
        if i % 2 == 0 and element % 2 != 0:
            result += element
    return result


# tests
assert(solution([5, 8, 7, 1]) == 12)
assert(solution([3, 3, 3, 3, 3]) == 9)
assert(solution([30, 13, 24, 321]) == 0)
print("All tests passed!")





# Solution:
# The function solution takes a list of integers as an argument. It initializes a variable result to 0. Then, using the enumerate function, it iterates over the list and for each element at even index (i % 2 == 0), it checks if the element is odd (element % 2 != 0). If both conditions are true, it adds the element to the result variable. Finally, it returns the result.

# The tests are provided to verify the correctness of the solution. The first test checks if the function correctly calculates the sum of odd elements at even positions for a list containing [5, 8, 7, 1]. The second test checks if the function correctly calculates the sum of all odd elements for a list containing [3, 3, 3, 3, 3]. The third test checks if the function correctly calculates the sum of odd elements at even positions for a list containing [30, 13, 24, 321]. The tests are expected to pass, indicating that the solution is correct.

# The time complexity of the solution is O(n), where n is the length of the input list. This is because the enumerate function is used to iterate over the list only once, and the if conditions are checked for each element in the list. The space complexity is O(1), as no additional data structures are used to store the input or intermediate results.





# The function solution takes a non-empty list of integers as an argument. It initializes a variable called result to 0. Then, using the enumerate function, it iterates over the list and for each element at an even index (i % 2 == 0