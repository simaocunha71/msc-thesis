```
const sortNumbers = (numbers) => {
  const numMap = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
  };
  const numbersArr = numbers.split(' ');
  const sortedNumbers = numbersArr.sort((a, b) => numMap[a] - numMap[b]);
  return sortedNumbers.join(' ');
};
```


Example usage:
```
console.log(sortNumbers('three one five'));  // Output: "one three five"
```


Explanation:

1. We create an object `numMap` that maps the string representation of numbers to their corresponding integer values.
2. We split the input string `numbers` into an array of strings using the space character as a delimiter.
3. We sort the array of strings using the `sort()` method and a callback function that compares the values in the `numMap` object.
4. We join the sorted array of strings back into a single string using the space character as a delimiter.
5. We return the sorted string.