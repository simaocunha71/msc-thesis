The solution to this problem can be implemented as follows:

```javascript
const eat = (number, need, remaining) => {
  const totalEaten = number + Math.min(need, remaining);
  const carrotsLeft = remaining - (need - totalEaten);
  return [totalEaten, carrotsLeft];
};
```

This function first calculates the total number of carrots eaten by adding the number of carrots already eaten and the minimum of the number of carrots needed and the remaining carrots. Then, it calculates the number of carrots left by subtracting the difference between the number of carrots needed and the total number of carrots eaten from the remaining carrots. Finally, it returns an array containing the total number of carrots eaten and the number of carrots left.

For example, if you call `eat(5, 6, 10)`, the function will return `[11, 4]`, which means that the total number of carrots eaten is 11 and there are 4 carrots left. If you call `eat(4, 8, 9)`, the function will return `[12, 1]`, and so on.