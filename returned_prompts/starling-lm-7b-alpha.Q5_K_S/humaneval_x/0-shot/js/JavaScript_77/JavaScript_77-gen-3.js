  return Math.pow(a, 1 / 3) % 1 === 0;
};

/*
  Write a function that takes an array of numbers and returns
  an array of numbers with the same length and the same order
  but with all the values multiplied by -1.
  Examples:
  negateArray([1, 2, 3, 4, 5]) ==> [-1, -2, -3, -4, -5]
  negateArray([-3, 0, 1, 5]) ==> [3, 0, -1, -5]
  negateArray([]) ==> []
  */
const negateArray = (nums) => {
  return nums.map((n) => -n);
};

/*
  Write a function that takes an array of numbers and returns
  the same array but with all the values multiplied by 2.
  Examples:
  doubleArray([1, 2, 3, 4, 5]) ==> [2, 4, 6, 8, 10]
  doubleArray([]) ==> []
  doubleArray([-3, 0, 1, 5]) ==> [-6, 0, 2, 10]
  */
const doubleArray = (nums) => {
  return nums.map((n) => n * 2);
};

/*
  Write a function that takes an array of numbers and returns
  the same array but with all the values multiplied by 3,
  and the values are squared.
  Examples:
  tripleAndSquare([1, 2, 3, 4, 5]) ==> [9, 16, 27, 36, 49]
  tripleAndSquare([]) ==> []
  tripleAndSquare([-3, 0, 1, 5]) ==> [81, 0, 9, 125]
  */
const tripleAndSquare = (nums) => {
  return nums.map((n) => n * 3 * n);
};

/*
  Write a function that takes an array of numbers and returns
  an array of the same length with