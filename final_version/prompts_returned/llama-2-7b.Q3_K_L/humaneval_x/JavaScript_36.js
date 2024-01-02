/*Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
  >>> fizzBuzz(50)
  0
  >>> fizzBuzz(78)
  2
  >>> fizzBuzz(79)
  3
  */
const fizzBuzz = (n) => {
  let i, count = 0;
  for (i=1 ; i<n ; i++) {
    if ((i%13 === 0 || i%11 === 0) && n % i !== 0) {
      count += 1;
    }
  }
  return count;
}