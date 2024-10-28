  const numA = parseFloat(a)
  const numB = parseFloat(b)

  if (numA === numB) return null

  return numA > numB ? a : b
}

console.log(compareOne(1, 2.5)) // ➞ 2.5
console.log(compareOne(1, "2,3")) // ➞ "2,3"
console.log(compareOne("5,1", "6")) // ➞ "6"
console.log(compareOne("1", 1)) // ➞ null
```

This program will convert the inputs to numbers and then compare them. If they are equal, it returns null. Otherwise, it returns the larger number (or string representation of a number) as a string. It assumes that the inputs are valid and does not handle invalid inputs.

In Javascript, the `>` operator will work with numbers and strings. If you compare two strings using `>`, it will compare them lexicographically. If you compare a string and a number, Javascript will try to convert the number to a string before comparing.

In the function `parseFloat`, we try to convert the inputs to numbers. If the conversion fails (for example, if the input is a string that can't be converted to a number), `parseFloat` will return `NaN`.

We then use the `>` operator to compare the numbers. If `numA` is greater than `numB`, we return `a`, otherwise we return `b`.

Here is another version of the function that handles invalid inputs:

```javascript
const compareOne = (a, b) => {
  const numA = parseFloat(a)
  const numB = parseFloat(b)

  if (isNaN(numA) || isNaN(numB)) return null

  return numA > numB ? a : b
}
```

In this version, we use the `isNaN` function to check if the inputs can be converted to numbers. If either `numA` or `numB` is `NaN`, we return null. Otherwise, we return the larger number as a string.

In this version, if the inputs