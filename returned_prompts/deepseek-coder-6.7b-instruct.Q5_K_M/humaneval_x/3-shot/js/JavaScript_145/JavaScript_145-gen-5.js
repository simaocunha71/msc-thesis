  return nums.sort((a, b) => {
    const sumDigits = (n) => Math.abs(n).toString().split('').reduce((sum, d) => sum + parseInt(d), 0);
    return sumDigits(a) - sumDigits(b) || nums.indexOf(a) - nums.indexOf(b);
  });
}



