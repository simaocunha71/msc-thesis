  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, cur) => acc + Math.abs(parseInt(cur)), 0);
    const sumB = b.toString().split('').reduce((acc, cur) => acc + Math.abs(parseInt(cur)), 0);

    if (sumA !== sumB) {
      return sumA - sumB;
    } else {
      return nums.indexOf(a) - nums.indexOf(b);
    }
  });
}



