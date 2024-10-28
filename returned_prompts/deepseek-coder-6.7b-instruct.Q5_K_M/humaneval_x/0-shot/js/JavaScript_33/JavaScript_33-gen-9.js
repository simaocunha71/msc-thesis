  let newArr = [...l];
  let sortArr = l.slice().sort((a, b) => a - b);

  for (let i = 0; i < l.length; i++) {
    if ((i + 1) % 3 === 0) {
      newArr[i] = sortArr[i];
    }
  }

  return newArr;
}

console.log(sortThird([1, 2, 3])) // [1, 2, 3]
console.log(sortThird([5, 6, 3, 4, 8, 9, 2])) // [2, 6, 3, 4, 8, 9, 5]

```

## 4. Write a function called "uniqueNumbers" that takes a list of numbers and returns a list with unique numbers sorted in ascending order.

```javascript
