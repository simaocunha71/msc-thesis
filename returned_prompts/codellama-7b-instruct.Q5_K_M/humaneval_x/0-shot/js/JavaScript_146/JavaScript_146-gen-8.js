/*Write a function that takes an array of numbers as input and returns 
  the number of elements in the array that are greater than 10 and both 
  first and last digits of a number are odd (1, 3, 5, 7, 9).
  For example:
  specialFilter([15, -73, 14, -15]) => 1 
  specialFilter([33, -2, -3, 45, 21, 109]) => 2
  */
const specialFilter = (nums) => {
  return nums.filter(num => num > 10 && (num.toString()[0] % 2 !== 0) && (num.toString()[num.toString().length - 1] % 2 !== 0)).length;
}

/*
//Another solution is to use reduce,

const specialFilter = (nums) => {
  return nums.reduce((acc, num) => {
    if (num > 10 && (num.toString()[0] % 2 !== 0) && (num.toString()[num.toString().length - 1] % 2 !== 0)) {
      acc++;
    }
    return acc;
  }, 0);
}

*/

/*
//Another solution is to use forEach

const specialFilter = (nums) => {
  let count = 0;
  nums.forEach(num => {
    if (num > 10 && (num.toString()[0] % 2 !== 0) && (num.toString()[num.toString().length - 1] % 2 !== 0)) {
      count++;
    }
  });
  return count;
}

*/

/*
//Another solution is to use find

const specialFilter = (nums) => {
  return nums.find(num => num > 10 && (num.toString()[0] % 2 !== 0) && (num.toString()[num.toString().length - 1] % 2 !== 0)) ? 1 : 0;
}

*/
