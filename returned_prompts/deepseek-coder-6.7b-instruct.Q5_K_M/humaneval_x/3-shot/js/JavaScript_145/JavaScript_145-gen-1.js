  const getSumOfDigits = (num) => {
    return Math.abs(num).toString().split('').reduce((sum, digit) => {
      return sum + parseInt(digit);
    }, 0);
  };

  return nums.slice().sort((a, b) => {
    const sumA = getSumOfDigits(a);
    const sumB = getSumOfDigits(b);

    if (sumA !== sumB) {
      return sumA - sumB;
    } else {
      return nums.indexOf(a) - nums.indexOf(b);
    }
  });
};



