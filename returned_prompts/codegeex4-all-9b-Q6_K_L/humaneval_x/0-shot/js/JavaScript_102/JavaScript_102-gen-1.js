You can solve this problem by checking if the numbers are even, if they are not, you increment them until you get an even number. Then you just compare which number is bigger, and return the biggest one.

Here's the solution:

```javascript
const chooseNum = (x, y) => {
  if (x > y) {
    let temp = x;
    x = y;
    y = temp;
  }

  while (x % 2 !== 0) {
    x++;
  }

  while (y % 2 !== 0) {
    y--;
  }

  if (x <= y) {
    return x;
  } else {
    return -1;
  }
}
```

This solution works by first checking if x is greater than y. If it is, it swaps the values of x and y. Then it increments x until it gets an even number, and it decrements y until it gets an even number. After that, it checks if x is less than or equal to y, if it is, it returns x, otherwise, it returns -1.