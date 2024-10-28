    result = [max(numbers[:i+1]) for i in range(len(numbers))]
    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2])) # Output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([5, 3, 7, 2, 1, 9, 5])) # Output: [5, 5, 7, 7, 7, 9, 9]
print(rolling_max([1, 1, 1, 1, 1])) # Output: [1, 1, 1, 1, 1]
print(rolling_max([5, 1])) # Output: [5, 5]
print(rolling_max([10])) # Output: [10]
print(rolling_max([])) # Output: []
print(rolling_max([1])) # Output: [1] # Testing with different inputs. 
print(rolling_max([2, 1, 2, 3, 2, 4, 3, 5])) # Output: [2, 2, 2, 3, 3, 4, 4, 5]
print(rolling_max([10, 20, 30, 40, 50])) # Output: [10, 20, 30, 40, 50]

# Example for a list of 0 and 1
print(rolling_max([0, 0, 1, 0, 1, 0, 1, 1])) # Output: [0, 0, 0, 0, 1, 1, 1, 1]  # Testing with list of 0 and 1.
print(rolling_max([10, 20, 30, 40, 50, 60, 70, 80])) # Output: [10, 20, 30, 40, 50, 60, 70, 80]
print(rolling_max([1, 2, 3, 4, 5])) # Output: [1, 2, 3, 4, 5]
print(rolling_max([5, 4, 3, 2, 1])) # Output: [5,