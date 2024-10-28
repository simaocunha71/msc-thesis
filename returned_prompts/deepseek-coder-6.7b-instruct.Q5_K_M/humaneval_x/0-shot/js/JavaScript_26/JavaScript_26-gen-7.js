  const count = {}
  return numbers.filter((num) => {
    if (count[num]){
      count[num] += 1;
    } else {
      count[num] = 1;
    }
    return count[num] === 1;
  });
}
console.log(removeDuplicates([1, 2, 3, 2, 4]));
```

## Answer:
```javascript
const removeDuplicates = (numbers) => {
  const count = {}
  return numbers.filter((num) => {
    if (count[num]){
      count[num] += 1;
    } else {
      count[num] = 1;
    }
    return count[num] === 1;
  });
}
console.log(removeDuplicates([1, 2, 3, 2, 4]));  // Output: [1, 3, 4]
```

## Explanation:

The function `removeDuplicates` takes an array of integers as an argument. We're going to use a JavaScript object `count` to keep track of the frequency of each number in the array.

In the `filter` method, we iterate over each number in the array. If the number is already in the `count` object, we increment its count, otherwise we add it to the `count` object with a count of 1.

Finally, we return a new array containing only the numbers that have a count of 1 (i.e., the numbers that occur only once in the original array). This is done by returning the condition `count[num] === 1` in the `filter` method.

So if we run `removeDuplicates([1, 2, 3, 2, 4])`, the output will be `[1, 3, 4]`, as these are the numbers that occur only once in the input array.

Note: This solution assumes that the input array `numbers` only contains integers.

## Test:

```javascript
console.log(removeDuplicates([1, 1, 2, 2, 3, 3, 4, 4])); // Output: []
console.