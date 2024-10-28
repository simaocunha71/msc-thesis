
def add_elements(arr, k):
    # Initialize sum to zero
    sum = 0
    # Loop through the first k elements of the array
    for i in range(k):
        # Check if the element is less than 100
        if len(str(arr[i])) <= 2:
            # Add the element to the sum
            sum += arr[i]
    # Return the sum
    return sum

# Time complexity: O(k)
# Space complexity: O(1)

# Alternative solution

def add_elements_alt(arr, k):
    sum = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum += arr[i]
    return sum

# Time complexity: O(k)
# Space complexity: O(1)

# Alternative solution

def add_elements_alt_2(arr, k):
    return sum(i for i in arr[:k] if len(str(i)) <= 2)

# Time complexity: O(k)
# Space complexity: O(1)

# Alternative solution

def add_elements_alt_3(arr, k):
    return sum(filter(lambda i: len(str(i)) <= 2, arr[:k]))

# Time complexity: O(k)
# Space complexity: O(1)

# Alternative solution

def add_elements_alt_4(arr, k):
    return sum(arr[:k], initial=0, key=lambda i: i if len(str(i)) <= 2 else 0)

# Time complexity: O(k)
# Space complexity: O(1)

# Alternative solution

def add_elements_alt_5(arr, k):
    return sum(i for i in arr[:k] if len(str(i)) <= 2, initial=0)

# Time complexity: O(k)
# Space complexity: O(1)

# Alternative solution

def add_elements_alt_6(arr, k):
    return sum(i for i in arr[:k] if len(str(i)) <= 