return a * b;

};

//Change the value of variable 'a' to test your function
var a = 148;
console.log(multiply(a, 412));

*/

/*

You are given an array of integers. Write a function that takes in an array of integers as a parameter and returns the sum of the even integers in the array. Assume the input is always valid.

Examples:
sumEvenIntegers([1, 2, 3, 4]) should return 6.
sumEvenIntegers([1, 3, 5, 6]) should return 6.
sumEvenIntegers([8, 9, 0, -10]) should return 18.
sumEvenIntegers([]) should return 0.

*/

function sumEvenIntegers(nums) {
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] % 2 === 0) {
      sum += nums[i];
    }
  }
  return sum;
}

// Change the value of variable 'nums' to test your function
var nums = [1, 2, 3, 4];
console.log(sumEvenIntegers(nums));

/*

You are given an array of integers. Write a function that takes in an array of integers as a parameter and returns the sum of the odd integers in the array. Assume the input is always valid.

Examples:
sumOddIntegers([1, 2, 3, 4]) should return 3.
sumOddIntegers([1, 3, 5, 6]) should return 9.
sumOddIntegers([8, 9, 0, -10]) should return 17.
sumOddIntegers([]) should return 0.

*/

function sumOddIntegers(nums) {
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i]