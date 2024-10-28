  nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((sum, digit) => sum + parseInt(digit), 0);
    const sumB = b.toString().split('').reduce((sum, digit) => sum + parseInt(digit), 0);
    if (sumA == sumB) {
      return a - b;
    }
    return sumA - sumB;
  });
  return nums;
}



