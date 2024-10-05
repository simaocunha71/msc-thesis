```
const sortArray = (array) => {
  const sum = array[0] + array[array.length - 1];
  if (sum % 2 === 0) {
    return array.slice().sort((a, b) => b - a);
  } else {
    return array.slice().sort((a, b) => a - b);
  }
};
```
Explanation:
* We calculate the sum of the first and last elements of the array.
* If the sum is even, we sort the array in descending order using the `sort()` method with a comparator function `(a, b) => b - a`.
* If the sum is odd, we sort the array in ascending order using the `sort()` method with a comparator function `(a, b) => a - b`.
* We use `slice()` to create a copy of the original array, since the problem statement asks us not to modify the original array.
* We return the sorted copy of the array.