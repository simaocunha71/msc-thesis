/*
  The first thing we need to do is define what an odd number is.
  An odd number is a number that is not divisible by 2.
  To check if a number is divisible by 2, we can take the modulo of that number.
  For example: 5 % 2 = 1, since 5 is not divisible by 2.
  To find the sum of the squares of all odd numbers in the list,
  we need to iterate through the list and check if each number is odd.
  If it is, we add its square to a running sum.
  */
const doubleTheDifference = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] % 2 !== 0) {
      sum += Math.pow(lst[i], 2);
    }
  }
  return sum;
};

B:
/*
  Instead of using a for loop, we can use map() and filter() to make our code more concise.
  We can use map() to change each number in the list to its square and filter() to
  remove any non-integer or negative numbers.
  */
const doubleTheDifference = (lst) => {
  return lst
    .map(x => Math.pow(x, 2))
    .filter(x => x % 1 === 0 && x >= 0)
    .reduce((a, b) => a + b, 0);
};

C:
/*
  We can also use the filter() method to find all the odd numbers in the list.
  Then we can use the map() method to square each of those numbers and use reduce()
  to sum the squares up.
  */
const doubleTheDifference = (lst) => {
  return lst
    .filter(x => x % 2 !== 0)
    .map(x => Math.pow(x, 2))
    .reduce((a, b) => a + b, 0);
};

D:
/*
  We can use the filter() method to find all the odd numbers in the list.
  Then we can use the map