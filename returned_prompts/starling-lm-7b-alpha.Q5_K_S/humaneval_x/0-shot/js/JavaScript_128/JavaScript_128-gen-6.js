
// 1
  const prod = arr.reduce((acc, curr) => {
    return acc * curr;
  }, 1);

// 2
  const isNegative = (num) => {
    return num < 0;
  };

// 3
  const sign = arr.filter(isNegative).length % 2 === 0 ? 1 : -1;

// 4
  const abs = arr.map((el) => {
    return Math.abs(el);
  });

// 5
  return prod * sign * abs.reduce((acc, curr) => {
    return acc + curr;
  });
};

/*
  In this solution, we first calculate the product of all numbers in the
  array by using the reduce method. Then, we define a function called isNegative
  to check if a number is negative or not. After that, we filter the array to get only
  the negative numbers and check if the length of this array is even or odd. If it's even,
  we assign the sign 1, otherwise we assign the sign -1. Then, we create a new array called
  'abs' with all the absolute values of the numbers in the original array. Finally, we calculate
  the sum of all the absolute values multiplied by the product of all the numbers and the sign.
*/

module.exports = prodSigns;






























































































































































































