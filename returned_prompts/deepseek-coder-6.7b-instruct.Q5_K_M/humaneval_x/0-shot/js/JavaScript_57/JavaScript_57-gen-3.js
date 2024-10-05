  let increasing = true;
  let decreasing = true;

B:
  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] > l[i + 1]) {
      increasing = false;
    }
    if (l[i] < l[i + 1]) {
      decreasing = false;
    }
  }

C:
  return increasing || decreasing;
}

D:
console.log(monotonic([1, 2, 4, 20])); // true
console.log(monotonic([1, 20, 4, 10])); // false
console.log(monotonic([4, 1, 0, -10])); // true

```

## 6. Sum of squares

Write a function that calculates the sum of squares of numbers in a list.

```javascript
const sumOfSquares = (l) => {
  let sum = 0;
  for (let i = 0; i < l.length; i++) {
    sum += Math.pow(l[i], 2);
  }
  return sum;
}

console.log(sumOfSquares([1, 2, 3])); // 14
```

## 7. Multiply even numbers

Write a function that multiplies all the even numbers in a list by 2.

```javascript
const multiplyEven = (l) => {
  for (let i = 0; i < l.length; i++) {
    if (l[i] % 2 === 0) {
      l[i] *= 2;
    }
  }
  return l;
}

console.log(multiplyEven([1, 2, 3, 4])); // [1, 4, 3, 8]
```

## 8. Average of even numbers

Write a function that calculates the average of even numbers in a list.

```javascript
const averageEven = (l) => {
  let sum = 0;
  let count = 0;
  for (let i = 0;