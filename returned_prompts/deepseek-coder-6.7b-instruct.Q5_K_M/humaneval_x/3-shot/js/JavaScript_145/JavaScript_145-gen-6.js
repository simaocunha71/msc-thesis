  const digitSum = (num) => Math.abs(num).toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
  return nums.slice().sort((a, b) => {
    const diff = digitSum(a) - digitSum(b);
    return diff === 0 ? nums.indexOf(a) - nums.indexOf(b) : diff;
  });
}



