/*
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 10 && (nums[i] % 10 === 1 || nums[i] % 10 === 3 || nums[i] % 10 === 5 || nums[i] % 10 === 7 || nums[i] % 10 === 9)) {
      count++;
    }
  }
  return count;
  */

  /*
  const evenNumbers = nums.filter((num) => num % 2 === 0);
  const oddNumbers = nums.filter((num) => num % 2 === 1);
  return evenNumbers.length + oddNumbers.length;
  */

  /*
  return nums.filter((num) => num > 10 && (num % 10 === 1 || num % 10 === 3 || num % 10 === 5 || num % 10 === 7 || num % 10 === 9)).length;
  */

  return nums.filter((num) => num > 10 && /^(1|3|5|7|9)$/.test(num % 10)).length;
}

specialFilter([15, -73, 14, -15]);
// 1
specialFilter([33, -2, -3, 45, 21, 109]);
// 2

/*
Write a function that takes a number as input and returns the number of 
  digits in the number.
  For example:
  numberOfDigits(1234) => 4
  numberOfDigits(123) => 3
  numberOfDigits(12) => 2
  numberOfDigits(1) => 1
  numberOfDigits(-1) => 1
  numberOfDigits(0) => 1
  */
const numberOfDigits = (num) => {
  return num.toString().length;
}

numberOfDigits(1234);
// 4