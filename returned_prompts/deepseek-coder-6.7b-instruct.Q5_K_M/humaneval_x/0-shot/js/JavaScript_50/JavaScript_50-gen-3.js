/*
  returns decoded string by shifting every character by 5 in the alphabet.
  */
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0) + 26) % 26) + "a".charCodeAt(0)
  )).join("");
}

/*
  takes as input string and returns string with every other character uppercase.
  */
const alternateCase = (s) => {
  return s.split("").map((ch, i) => i % 2 === 0 ? ch.toUpperCase() : ch.toLowerCase()).join("");
}
```

## Task 3:

```js
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
const array3 = [7, 8, 9];

const arrays = [array1, array2, array3];

// Use the reduce method to flatten the arrays.
const flattenedArrays = arrays.reduce((accumulator, currentValue) => {
  return accumulator.concat(currentValue);
}, []);

console.log(flattenedArrays); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Task 4:

```js
const array = [1, 2, 3, 4, 5];

// Use the filter method to create a new array with only the even numbers.
const evenNumbers = array.filter(number => number % 2 === 0);

console.log(evenNumbers); // Output: [2, 4]
```

## Task 5:

```js
const array = [1, 2, 3, 4, 5];

// Use the map method to create a new array with the square of each number.
const squaredNumbers = array.map(number => number * number);

console.log(squaredNumbers); // Output: [1