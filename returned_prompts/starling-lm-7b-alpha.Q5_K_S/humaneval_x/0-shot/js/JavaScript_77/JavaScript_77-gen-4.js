return Math.pow(Math.pow(Math.pow(a, 1 / 3), 3), 3) === a;
};

/*
  Write a function that takes an array and an integer and
  returns an array with the same length as the input array
  but with the value at index i replaced by the value at index i from the input array,
  multiplied by the integer passed as the argument.
  Examples:
  multiply_by(2, [1, 2, 3]) ==> [2, 4, 6]
  multiply_by(-1, [1, 2, 3]) ==> [-1, -2, -3]
  multiply_by(0, [1, 2, 3]) ==> [0, 0, 0]
  multiply_by(3, [1, 2, 3]) ==> [3, 6, 9]
  */
const multiply_by = (b, c) => {

B:
return c.map((d, i) => b * d);
};

/*
  Write a function that takes an integer n and returns
  the sum of the cubes of the first n natural numbers.
  Examples:
  sum_cubes(1) ==> 1
  sum_cubes(2) ==> 5
  sum_cubes(3) ==> 24
  sum_cubes(4) ==> 67
  sum_cubes(5) ==> 130
  */
const sum_cubes = (e) => {

C:
return e * (e + 1) * (2 * e + 1) / 6;
};

/*
  Write a function that takes an array and an integer and
  returns the sum of the values at the indices i and i + 1
  in the input array, multiplied by the integer passed as the argument.
  Examples:
  sum_by(2, [1, 2, 3]) ==> 10
  sum_by(3, [1, 2, 3]) ==> 15
  sum_by(4, [1, 2, 3]) ==> 2