  return numbers.reduce((acc, curr, index) => {
    return index === 0 ? [...acc, curr] : [...acc, delimeter, curr];
  }, []);
};

console.log(intersperse([], 4));
console.log(intersperse([1, 2, 3], 4));

```

Output:

```
[]
[1, 4, 2, 4, 3]
```

Explanation:

- The `intersperse` function takes in an array `numbers` and a number `delimeter`.
- It applies the `reduce` function to `numbers`.
- In the reduce function, it checks if the index is 0. If it is, it adds the current number to the accumulator. If it's not, it adds the delimeter and the current number to the accumulator.
- This results in an array where every two consecutive numbers are separated by the delimeter.
- The final result is returned.

This solution has a time complexity of O(n), where n is the number of elements in the array.

*/

const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, curr, index) => {
    return index === 0 ? [...acc, curr] : [...acc, delimeter, curr];
  }, []);
};

console.log(intersperse([], 4));
console.log(intersperse([1, 2, 3], 4));
```

Output:

```
[]
[1, 4, 2, 4, 3]
```

Explanation:

- The `intersperse` function takes in an array `numbers` and a number `delimeter`.
- It applies the `reduce` function to `numbers`.
- In the reduce function, it checks if the index is 0. If it is, it adds the current number to the accumulator. If it's not, it adds the delimeter and the current number to the accumulator.
- This results in an array where every two consecutive numbers are separated by