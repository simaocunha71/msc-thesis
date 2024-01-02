/*The Brazilian factorial is defined as:
  brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
  where n > 0

  For example:
  >>> specialFactorial(4)
  288

  The function will receive an integer as input and should return the special
  factorial of this integer.
  */
const specialFactorial = (n) => {
    let fact = 1;
    for (let i=0,j=1; j<n+1;i++, j++)
        fact *= n-i;
    return fact;
}

module.exports = specialFactorial