/*
  let counter = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 10 && ((nums[i] % 10) % 2) === 1 && (nums[i] % 100) % 2 === 1) {
      counter++;
    }
  }
  return counter;
*/
const specialFilter = (nums) => {
  return nums.filter(num => num > 10 && ((num % 10) % 2) === 1 && (num % 100) % 2 === 1).length;
};

/*
  const specialFilter = (nums) => {
    return nums.reduce((acc, num) => {
      if (num > 10 && ((num % 10) % 2) === 1 && (num % 100) % 2 === 1) {
        acc++;
      }
      return acc;
    }, 0);
  };
*/

/*
  const specialFilter = (nums) => {
    return nums.filter(num => num > 10 && ((num % 10) % 2) === 1 && (num % 100) % 2 === 1).length;
  };
*/






























































































































































































