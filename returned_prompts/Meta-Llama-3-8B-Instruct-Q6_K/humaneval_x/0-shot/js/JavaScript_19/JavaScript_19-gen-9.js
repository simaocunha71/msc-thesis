```javascript
const sortNumbers = (numbers) => {
  const numMap = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
  };
  const nums = numbers.split(' ');
  const sortedNums = nums.sort((a, b) => numMap[a] - numMap[b]);
  return sortedNums.join(' ');
};
```


Explanation:
We create an object `numMap` that maps each number word to its corresponding integer value. Then we split the input string into an array of words `nums` and sort it using the `sort` method with a compare function that uses `numMap`. Finally, we join the sorted array back into a string and return it.