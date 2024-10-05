```
const sortArray = (array) => {
  const firstLastSum = array[0] + array[array.length - 1];
  const isOdd = firstLastSum % 2 !== 0;
  const sortedArray = array.slice();

  if (isOdd) {
    sortedArray.sort((a, b) => a - b);
  } else {
    sortedArray.sort((a, b) => b - a);
  }

  return sortedArray;
};
```


Explanation:
We first calculate the sum of the first and last elements of the array. If the sum is odd, we sort the array in ascending order. If the sum is even, we sort the array in descending order. We use the `slice()` method to create a copy of the original array, so the original array remains unchanged. We then use the `sort()` method with a compare function to sort the array accordingly. Finally, we return the sorted array.