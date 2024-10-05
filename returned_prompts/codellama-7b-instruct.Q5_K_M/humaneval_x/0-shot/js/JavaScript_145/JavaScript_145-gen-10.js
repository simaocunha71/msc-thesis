const orderByPoints = (nums) => nums.sort((a, b) => {
  const sumA = a.toString().split('').reduce((acc, curr) => acc + +curr, 0);
  const sumB = b.toString().split('').reduce((acc, curr) => acc + +curr, 0);
  if (sumA === sumB) return nums.indexOf(a) - nums.indexOf(b);
  return sumA - sumB;
});

