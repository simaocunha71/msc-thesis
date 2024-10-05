```
const sortNumbers = (numbers) => {
  const numMap = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9
  };
  const nums = numbers.split(' ');
  const sortedNums = nums.sort((a, b) => {
    return numMap[a] - numMap[b];
  });
  return sortedNums.join(' ');
};
```


In this solution, we first create an object `numMap` where the keys are the number strings and the values are the corresponding integer values.

Then, we split the input string `numbers` into an array of strings `nums` using the space character as a delimiter.

Next, we sort the array `nums` using the `sort` method with a compare function. The compare function uses the `numMap` object to convert each string to an integer and compare them.

Finally, we join the sorted array back into a string using the space character as a delimiter and return the result.