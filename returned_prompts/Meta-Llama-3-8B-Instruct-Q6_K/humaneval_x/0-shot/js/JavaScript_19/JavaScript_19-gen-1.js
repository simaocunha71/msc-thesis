```
const sortNumbers = (numbers) => {
  const numMap = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
  };
  return numbers.split(' ').sort((a, b) => numMap[a] - numMap[b]).join(' ');
};
```


Explanation:

1. We create an object `numMap` to map the string representations of numbers to their corresponding integer values.

2. We split the input string `numbers` into an array of strings using the `split` method with a space character as the separator.

3. We sort the array of strings using the `sort` method and a compare function that takes two strings `a` and `b` as arguments. The compare function returns the difference between the integer values corresponding to `a` and `b` in the `numMap` object.

4. Finally, we join the sorted array of strings back into a single string using the `join` method with a space character as the separator.

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the number of numbers in the input string. The space complexity is O(1) as we only use a constant amount of space to store the `numMap` object and the sorted array.