  return l.filter(n => n > 0);
};

console.log(getPositive([-1, 2, 4, 5, 6]))
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))

```

The function `getPositive` takes an array `l` and filters it to only include numbers that are greater than 0. The arrow function `n => n > 0` returns true if a number `n` is greater than 0, and false otherwise. The `filter` function then returns a new array that only includes the numbers for which the arrow function returned true.

This function can be used to filter out any negative or zero numbers from an array, leaving only the positive numbers.

We use `console.log` to print the results of the function calls to the console.
*/

// This is a JavaScript code snippet that filters out negative and zero numbers from an array and returns only positive numbers.
// It uses a built-in JavaScript method called 'filter' which creates a new array with all elements that pass the test implemented by the provided function.
// The function checks if each number in the array is greater than 0, if yes, it is included in the new array.
// The 'filter' method does not mutate the original array.
// The arrow function 'n => n > 0' is a compact way to write a function that checks if a number is greater than 0.
// The result is printed to the console using 'console.log'.
// This code can be used as a part of a larger JavaScript program.
const getPositive = (l) => {
  return l.filter(n => n > 0);
};

console.log(getPositive([-1, 2, -4, 5, 6])) // [2, 5, 6]
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) // [5, 3, 2, 3, 9, 123, 1]
```

The