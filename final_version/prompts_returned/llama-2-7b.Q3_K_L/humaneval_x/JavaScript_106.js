/* Implement the function f that takes n as a parameter,
  and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
  or the sum of numbers from 1 to i otherwise.
  i starts from 1.
  the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
  Example:
  f(5) == [1, 2, 6, 24, 15]
  */
const f = (n) => {
  let array = [];
  for (let i = 0; i <= n; i++) {
    if (i % 2 !== 0) {
      array[i - 1] = array[i - 1] + 1;
    } else {
      array[i - 1] = Math.factorial(i);
    }
  }

  return array;
};
// Example: f(2) == [1, 2]; f(3) == [1, 6, 15]
// Factorial of i is defined as follows: the multiplication of numbers from 1 to i.
// Factorial of 0 = 1; and factorial of -n is undefined.
function MathFactorial(i){
  if (i === 0) return 1;
  else return i * MathFactorial(i-1); 
};
