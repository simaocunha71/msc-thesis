  return nums.sort((a, b) => {
    const sumA = a.toString().split('').map(Number).reduce((a, b) => a + b, 0);
    const sumB = b.toString().split('').map(Number).reduce((a, b) => a + b, 0);
    return sumA - sumB || nums.indexOf(a) - nums.indexOf(b);
  });
}



