
return nums.map(num => {
  return num % 2 === 0 ? true : false;
});
};




/*
  Given an array of numbers, return an array of the same size containing
  whether each number is a prime number or not.

  A prime number is only divisible by 1 and itself. For example, 2, 3, 5,
  7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
  79, 83, 89 and 97 are the first 20 prime numbers. (Note: 0 and 1 are not
   prime numbers).

  For example:
  isPrimeNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 