/*Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
  >>> fizzBuzz(50)
  0
  >>> fizzBuzz(78)
  2
  >>> fizzBuzz(79)
  3
  */
const fizzBuzz = (n) => {
  let i, res = [];
  for (i=1;i<n;i+=2){res.push('Fizz'+i+'Buzz')};
  return res;
}
console.log(fizzBuzz(50));