  let deriv = []
  for(let i = 1; i < xs.length; i++){
    deriv.push(xs[i]*i)
  }
  return deriv;
}

console.log(derivative([3, 1, 2, 4, 5])) // [1, 4, 12, 20]
console.log(derivative([1, 2, 3])) // [2, 6]
```

This code uses a for loop to iterate over the coefficients of the polynomial. For each coefficient, it multiplies it by the index (which represents the power of x for that coefficient) and adds the result to the new array "deriv".

The result is the coefficients of the derivative of the polynomial.

For instance, if the coefficients of the polynomial are [3, 1, 2, 4, 5], the derivative will have coefficients [1, 4, 12, 20], because 1*1 + 4*2 + 12*3 + 20*4 = 3x + 4x^2 + 12x^3 + 20x^4.

If the coefficients of the polynomial are [1, 2, 3], the derivative will have coefficients [2, 6], because 2*1 + 6*2 = 2x + 6x^2.

This code assumes that the input is always an array of numbers with at least one element.

It also assumes that the coefficients are given in the form of the polynomial [3, 1, 2, 4, 5] where 3 is coefficient of x^0, 1 is coefficient of x^1, 2 is coefficient of x^2 and so on.






















































































































