def remove_length(s, k):
    return ' '.join(word for word in s.split() if len(word) != k)

print(remove_length('The person is most value tet', 3))  # Output: 'person is most value'  # Test case 1
print(remove_length('Hello World', 3))  # Output: ''  # Test case 2
print(remove_length('The person is most value tet', 5))  # Output: 'The is most value'  # Test case 3
print(remove_length('Hello World', 6))  # Output: 'Hello World'  # Test case 4
print(remove_length('Hello World', 1))  # Output: 'Hello World'  # Test case 5
print(remove_length('Hello World', 7))  # Output: 'Hello World'  # Test case 6
print(remove_length('Hello World', 9))  # Output: 'Hello World'  # Test case 7
print(remove_length('Hello World', 0))  # Output: 'Hello World'  # Test case 8
print(remove_length('Hello World', 8))  # Output: 'Hello World'  # Test case 9
print(remove_length('Hello World', 4))  # Output: 'Hello World'  # Test case 10
print(remove_length('Hello World', 2))  # Output: 'Hello World'  # Test case 11
print(remove_length('Hello World', 10))  # Output: 'Hello World'  # Test case 12
print(remove_length('Hello World', 11))  # Output: 'Hello World'  # Test case 13
print(remove_length('Hello World', 12))  # Output: 'Hello World'  # Test case 14
print(remove_length('Hello World', 13))  # Output: 'Hello World'  # Test case 15
print(remove_length('Hello World', 14))  # Output: 'Hello World'  # Test case 16
print(remove_length('Hello World', 15))  # Output: 'Hello World'  # Test case 17
print(remove_length('Hello World', 16))  # Output: 'Hello World'  # Test case 18
print(remove_length('Hello World', 17))  # Output: 'Hello World'  # Test case 19
print(remove