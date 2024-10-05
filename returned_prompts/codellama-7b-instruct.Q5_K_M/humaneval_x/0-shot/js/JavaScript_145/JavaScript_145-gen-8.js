const orderByPoints = (nums) => {
  const sorted = nums.slice().sort((a, b) => {
    const sumA = a.toString().split('').reduce((s, c) => s + +c, 0);
    const sumB = b.toString().split('').reduce((s, c) => s + +c, 0);
    if (sumA === sumB) return a - b;
    return sumA - sumB;
  });
  return sorted;
}

