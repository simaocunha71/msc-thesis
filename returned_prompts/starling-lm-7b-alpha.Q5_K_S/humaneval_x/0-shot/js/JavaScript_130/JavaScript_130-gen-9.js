
let result = [3];
if (n === 0) return result;

while (n > 0) {
  if (n % 2 === 0) {
    result.push(result[result.length - 1]);
  } else {
    let prev3 = result[result.length - 1];
    let prev2 = result[result.length - 2];
    let prev1 = result[result.length - 3];
    result.push(prev3 + prev2 + prev1);
  }
  n--;
}
return result;
};

*/

/*
  The sum of the squares of the first n natural numbers is given by the formula n(n+1)(2n+1)/6,
  prove this using mathematical induction.

  Let P(n) be the statement "The sum of the squares of the first n natural numbers is
  given by the formula n(n+1)(2n+1)/6"

  Base case:
  Prove P(0) is true:
  The sum of the squares of the first 0 natural numbers is 0, and 0(0+1)(2(0)+1)/6 = 0

  Inductive step:
  Assume P(k) is true for some natural number k, that is,
  the sum of the squares of the first k natural numbers is k(k+1)(2k+1)/6
  Prove P(k+1) is true, that is,
  Prove the sum of the squares of the first k+1 natural numbers is (k+1)(k+2)(2(k+1)+1)/6

  Sum of squares of first k+1 natural numbers = (sum of squares of first k natural numbers) + ((k+1)^2)
  = (k(k+1)(2k+1)/6) + ((k+1)^2)
  = (2k^2 + 3k + 1) + (2k^2 + 3k + 1)
  = 4k^2 + 6k + 2
  = (k+1)(k+2)(2(k+1) + 1