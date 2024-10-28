  // split the fractions
  const [xNum, xDen] = x.split('/')
  const [nNum, nDen] = n.split('/')

  // calculate the new numerators
  const newNum = xNum * nNum
  const newDen = xDen * nDen

  // check if new numerator is a whole number
  return newNum % 1 === 0
}

console.log(simplify("1/5", "5/1")) // true
console.log(simplify("1/6", "2/1")) // false
console.log(simplify("7/10", "10/2")) // false

/*This code works by first splitting the input fractions into their numerator and denominator
parts. Then it calculates the new numerator by multiplying the numerators of the two
fractions together, and the new denominator by multiplying the denominators of the two
fractions together. Finally, it checks if the new numerator is a whole number by seeing if
it is evenly divisible by 1 (i.e., has no remainder). It returns true if it is, and false otherwise.*/
```

## Solution 02:

```js
