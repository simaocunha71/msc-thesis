const specialFilter = (nums) => {
  const isOdd = (num) => (Math.abs(num) % 10).toString().split('')[0] % 2 === 1;
  return nums.filter(num => num > 10 && isOdd(num)).length;
};

