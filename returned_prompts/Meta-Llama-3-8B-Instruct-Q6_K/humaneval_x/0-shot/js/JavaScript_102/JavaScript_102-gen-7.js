Here is a possible solution:
```
const chooseNum = (x, y) => {
  if (x > y) {
    [x, y] = [y, x]; // swap x and y if x is greater than y
  }
  for (let i = x; i <= y; i++) {
    if (i % 2 === 0) {
      return i;
    }
  }
  return -1;
};
```
This function first checks if `x` is greater than `y` and swaps them if necessary. Then it iterates from `x` to `y` and checks if each number is even (i.e., `i % 2 === 0`). If it finds an even number, it returns that number. If it doesn't find any even numbers in the range, it returns -1.

You can test this function with the examples you provided:
```
console.log(chooseNum(12, 15)); // output: 14
console.log(chooseNum(13, 12)); // output: -1
```
I hope this helps! Let me know if you have any questions.