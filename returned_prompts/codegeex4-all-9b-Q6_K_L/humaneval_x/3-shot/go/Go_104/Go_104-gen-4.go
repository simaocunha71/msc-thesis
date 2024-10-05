
SeparateParenGroups

The main bottleneck in this function is the conversion of current_string to string. This is done in every iteration, which is unnecessary. You can create a single byte slice and use the append function to add runes to it. Once the group is done, you can convert it to a string and append it to the result slice.
The current implementation has a time complexity of O(n^2) because it uses nested loops to compare each pair of numbers. This can be optimized to O(n) by using a single loop and a hash map to store the count of each number.
The current implementation has a space complexity of O(n) because it uses a slice to store the result. This can be optimized to O(1) by using a single integer variable to store the count of unique numbers.

TruncateNumber

The current implementation has a time complexity of O(1) because it uses a built-in function to calculate the modulus. This cannot be optimized further.

UniqueDigits

The current implementation has a time complexity of O(n^2) because it uses nested loops to iterate over the list and each number. This can be optimized to O(n) by using a single loop and a hash map to store the count of each number.
The current implementation has a space complexity of O(n) because it uses a slice to store the result. This can be optimized to O(1) by using a single integer variable to store the count of unique numbers.