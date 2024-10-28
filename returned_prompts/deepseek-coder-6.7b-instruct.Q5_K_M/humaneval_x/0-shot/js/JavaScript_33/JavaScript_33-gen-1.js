  let result = [];
  let nonDivByThree = [];

  for(let i = 0; i < l.length; i++) {
    if(i % 3 === 0) {
      nonDivByThree.push(l[i]);
      result.push('x');
    } else {
      result.push(l[i]);
    }
  }

  nonDivByThree.sort((a, b) => a - b);

  for(let i = 0; i < result.length; i++) {
    if(i % 3 === 0) {
      result[i] = nonDivByThree.shift();
    }
  }

  return result;
};

console.log(sortThird([1, 2, 3])); // [1, 2, 3]
console.log(sortThird([5, 6, 3, 4, 8, 9, 2])); // [2, 6, 3, 4, 8, 9, 5]

```



## 2. Fibonacci Sequence

### Problem:
Write a function that returns the first n numbers in the Fibonacci sequence.

### Solution:
Here is a simple solution in JavaScript:

```javascript
// 