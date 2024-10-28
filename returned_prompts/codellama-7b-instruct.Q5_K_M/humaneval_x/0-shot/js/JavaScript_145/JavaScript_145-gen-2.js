const orderByPoints = (nums) => {
  return nums.sort((a, b) => {
    const sumA = (a + '').split('').reduce((acc, digit) => acc + Number(digit), 0);
    const sumB = (b + '').split('').reduce((acc, digit) => acc + Number(digit), 0);
    if (sumA === sumB) {
      return a - b;
    }
    return sumA - sumB;
  });
};
