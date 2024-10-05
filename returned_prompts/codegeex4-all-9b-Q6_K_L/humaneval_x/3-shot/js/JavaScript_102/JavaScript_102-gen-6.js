
You need to find the biggest even number within the range [x, y] inclusive. If there's no such number, return -1.

This can be done using a loop, starting from x and incrementing by 2 (since we're looking for even numbers) until we reach or pass y. If we reach or pass y without finding an even number, return -1. Otherwise, return the number we found.

Here's the code:
```javascript
const chooseNum = (x, y) => {
  for (let i = x; i <= y; i += 2) {
    return i;
  }
  return -1;
}
```

If you want to make it more efficient, you can start from the biggest even number less than or equal to y and decrement by 2 until you reach or pass x. If you reach or pass x without finding an even number, return -1. Otherwise, return the number we found.

Here's the code:
```javascript
const chooseNum = (x, y) => {
  for (let i = y; i >= x; i -= 2) {
    return i;
  }
  return -1;
}
```

These both should give you the same results, but the second one is more efficient if y is much larger than x.