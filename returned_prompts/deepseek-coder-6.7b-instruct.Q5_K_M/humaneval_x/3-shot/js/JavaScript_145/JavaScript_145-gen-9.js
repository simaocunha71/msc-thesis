  return nums.sort((a, b) => {
    const sumA = String(Math.abs(a)).split('').reduce((acc, v) => acc + Number(v), 0);
    const sumB = String(Math.abs(b)).split('').reduce((acc, v) => acc + Number(v), 0);
    if (sumA !== sumB) {
      return sumA - sumB;
    }
    return nums.indexOf(a) - nums.indexOf(b);
  });
}



