def is_samepatterns(patterns1, patterns2):
    if len(patterns1) != len(patterns2):
        return False
    for i in range(len(patterns1)):
        if patterns1[i] != patterns2[i]:
            return False
    return True


# Test
print(is_samepatterns(["red","green","green"], ["a", "b", "b"]))

"""
Explanation:
In the above code, the function `is_samepatterns` takes in two arrays `patterns1` and `patterns2`.
The function first checks if the lengths of `patterns1` and `patterns2` are equal. If they are not equal, it returns False, as the patterns cannot be the same.
Then, the function iterates over each element of the arrays using a for loop. For each element at index `i`, it checks if the element at index `i` in `patterns1` is equal to the element at index `i` in `patterns2`. If any of the elements are not equal, the function returns False.
If all the elements are equal, the function returns True, indicating that the patterns are the same.
"""

# Usage Example:

def main():
    patterns1 = ["red", "green", "green"]
    patterns2 = ["a", "b", "b"]
    result = is_samepatterns(patterns1, patterns2)
    print(result)

if __name__ == "__main__":
    main()


"""
Explanation:
In the above code, the function `main` is defined. Inside the function, two arrays `patterns1` and `patterns2` are defined. The `is_samepatterns` function is then called with `patterns1` and `patterns2` as arguments, and the result is stored in the variable `result`. Finally, the result is printed to the console.
"""

"""
Explanation:
In the above code, the `if __name__ == "__main__":` block is used to ensure that the `main` function is only executed when the Python script is run directly (not imported as a module). This allows the code to be tested and executed independently of other parts