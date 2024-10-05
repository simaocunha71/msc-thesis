function concatenate(strings) {
  return strings.reduce((acc, current) => acc + current, '');
}

// Test cases
console.log(concatenate([]));  // ''
console.log(concatenate(['a', 'b', 'c']));  // 'abc'

// Explanation:
The function `concatenate` takes a list of strings as input and returns a single string that is the concatenation of all the strings in the list.
The `reduce` method is used to concatenate the strings. It takes two arguments: a callback function and an initial value. The callback function is called for each element in the list, and it returns the result of concatenating the current element with the accumulator (which is initialized to an empty string). The `reduce` method returns the final result, which is the concatenated string.