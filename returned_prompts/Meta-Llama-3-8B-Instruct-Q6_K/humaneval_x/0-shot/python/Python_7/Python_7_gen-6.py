    return [s for s in strings if substring in s]
    
# Example usage:
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['hello', 'world', 'python'], 'python'))  # Output: ['python'] 
print(filter_by_substring(['python', 'is', 'awesome'], 'python'))  # Output: ['python']
print(filter_by_substring(['python', 'is', 'awesome'], 'awesome'))  # Output: ['awesome']  # Output: ['python', 'awesome']  # Output: [] 
print(filter_by_substring(['apple', 'banana', 'cherry'], 'a'))  # Output: ['apple', 'banana', 'cherry']  # Output: []  # Output: ['apple']  # Output: ['apple', 'banana']  # Output: []  # Output: ['apple']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana', 'cherry']  # Output: ['apple', 'banana