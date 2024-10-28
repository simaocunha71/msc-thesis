  let sequence = '';
  for (let i = 0; i <= n; i++) {
    sequence += i + ' ';
  }
  return sequence.trim();
}

console.log(stringSequence(0));
console.log(stringSequence(5));
```

### JavaScript 1.6 `map` method

The `map` method creates a new array with the result of calling a provided function on every element in the calling array.

```javascript
let numbers = [1, 2, 3, 4, 5];
let squares = numbers.map(n => n * n);
console.log(squares); // [1, 4, 9, 16, 25]
```

In this example, `map` is called on an array of numbers. It calls the arrow function `n => n * n` on each element of the array, effectively squaring each number. The result is a new array, `squares`, containing the squares of the original numbers.

### JavaScript 1.7 `filter` method

The `filter` method creates a new array with all elements that pass the test implemented by the provided function.

```javascript
let numbers = [1, 2, 3, 4, 5];
let evenNumbers = numbers.filter(n => n % 2 === 0);
console.log(evenNumbers); // [2, 4]
```

In this example, `filter` is called on an array of numbers. It calls the arrow function `n => n % 2 === 0` on each element of the array, effectively filtering out the odd numbers. The result is a new array, `evenNumbers`, containing only the even numbers from the original array.

### JavaScript 1.8 `reduce` method

The `reduce` method executes a reducer function on each element of the array, resulting in a single output value.

```javascript
let numbers = [1, 2, 3, 4, 5];
let sum = numbers.reduce((total, n) => total + n, 0);
console.log(sum); // 15
```

In this example, `reduce` is called on an array of numbers