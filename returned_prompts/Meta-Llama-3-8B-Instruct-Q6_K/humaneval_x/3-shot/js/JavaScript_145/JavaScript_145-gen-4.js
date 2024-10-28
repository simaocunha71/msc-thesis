  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    const sumB = b.toString().split('').reduce((acc, cur) => acc + parseInt(cur), 0);
    return sumA - sumB || nums.indexOf(a) - nums.indexOf(b);
  });
}