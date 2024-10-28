Here is the solution for the problem:

```javascript
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

  const sortedNums = numbers.split(' ').sort((a, b) => {
    return numMap[a] - numMap[b];
  });

  return sortedNums.join(' ');
};

console.log(sortNumbers('three one five'));  // Output: "one three five"
```

Explanation:

1.  We create an object `numMap` that maps each number word to its corresponding integer value.
2.  We split the input string `numbers` into an array of words using the `split()` method.
3.  We use the `sort()` method to sort the array of words. The comparison function `(a, b) => numMap[a] - numMap[b]` is used to compare the words based on their corresponding integer values.
4.  We join the sorted array of words back into a string using the `join()` method with a space character as the separator.
5.  Finally, we return the sorted string. In this case, the output is `"one three five"`.