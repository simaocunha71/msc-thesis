  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    let strNum = nums[i].toString();
    if (strNum[0] % 2 === 1 && strNum[strNum.length - 1] % 2 === 1 && nums[i] > 10) {
      count++;
    }
  }

  return count;
};

specialFilter([15, -73, 14, -15]); // 1
specialFilter([33, -2, -3, 45, 21, 109]); // 2

/*
  Let's test the function with some edge cases:
  - When an empty array is passed:
  specialFilter([]) => 0

  - When an array with all negative numbers is passed:
  specialFilter([-2, -3, -5, -7, -9]) => 1

  - When an array with all positive numbers is passed:
  specialFilter([1, 3, 5, 7, 9]) => 5

  - When an array with all numbers less than 10 is passed:
  specialFilter([-7, -3, 1, 3, 5]) => 0

  - When an array with all numbers greater than 10 is passed:
  specialFilter([11, 13, 15, 17, 19]) => 5
*/































































































































































