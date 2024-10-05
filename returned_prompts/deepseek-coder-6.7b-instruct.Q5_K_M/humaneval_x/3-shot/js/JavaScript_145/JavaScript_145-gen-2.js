  return nums.sort((a, b) => {
    let sumA = a.toString().split('').map(Number).reduce((a, b) => a + b, 0);
    let sumB = b.toString().split('').map(Number).reduce((a, b) => a + b, 0);
    return sumA - sumB || nums.indexOf(a) - nums.indexOf(b);
  });
}



