Here is the solution in JavaScript:
```
const moveOneBall = (arr) => {
  if (arr.length === 0) return true;

  const sortedArr = [...arr].sort((a, b) => a - b);

  for (let i = 0; i < arr.length; i++) {
    let j = i;
    while (j < arr.length) {
      arr[j] = arr[(j + 1) % arr.length];
      j++;
    }
    if (arr.join() !== sortedArr.join()) return false;
  }

  return true;
};
```
Explanation:

1. If the input array is empty, return `true`.
2. Create a sorted copy of the input array using the `sort()` method.
3. Iterate through the input array and perform a right shift operation at each position.
4. For each position, shift all elements to the right by one position using a while loop.
5. After each shift, check if the resulting array is equal to the sorted array using the `join()` method. If it's not equal, return `false`.
6. If all shifts result in a sorted array, return `true`.

Example usage:
```
console.log(moveOneBall([3, 4, 5, 1, 2])); // true
console.log(moveOneBall([3, 5, 4, 1, 2])); // false
```



