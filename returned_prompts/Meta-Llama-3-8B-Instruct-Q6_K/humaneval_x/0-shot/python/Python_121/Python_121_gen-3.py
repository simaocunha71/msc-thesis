    # Initialize the sum to 0
    total = 0
    
    # Iterate over the list with enumerate to get both index and value
    for i, num in enumerate(lst):
        # Check if the index is even and the number is odd
        if i % 2 == 0 and num % 2 != 0:
            # Add the number to the total
            total += num
    
    # Return the total
    return total

# Test cases
print(solution([5, 8, 7, 1])) # 12
print(solution([3, 3, 3, 3, 3])) # 9
print(solution([30, 13, 24, 321])) # 0
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 16
print(solution([10, 20, 30, 40, 50, 60, 70, 80, 90])) # 0
print(solution([1, 3, 5, 7, 9, 2, 4, 6, 8])) # 25
print(solution([2, 4, 6, 8, 10, 12, 14, 16, 18])) # 0
print(solution([3, 5, 7, 9, 1, 3, 5, 7, 9])) # 36
print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1])) # 9
print(solution([2, 2, 2, 2, 2, 2, 2, 2, 2])) # 0
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 16
print(solution([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) # 0
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # 36
print(solution