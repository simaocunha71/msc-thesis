def by_length(arr):
    num_dict = {str(i): val for i, val in enumerate(range(1, 10), start=1)}
    arr = [i for i in arr if 1 <= i <= 9]
    arr.sort()
    arr = arr[::-1]
    return [num_dict[str(i)] for i in arr] if arr else []

# Testing the function
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # Expected output: ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
print(by_length([]))  # Expected output: []
print(by_length([1, -1, 55]))  # Expected output: ['One']














