  return nums.sort((a, b) => {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    const sumA = a.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    const sumB = b.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    if (sumA < sumB) return -1;
    if (sumA > sumB) return 1;
    return nums.indexOf(a) - nums.indexOf(b);
  });
} 



