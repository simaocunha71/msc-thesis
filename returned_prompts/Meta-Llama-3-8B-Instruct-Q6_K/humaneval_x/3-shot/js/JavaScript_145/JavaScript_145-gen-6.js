  nums.sort((a, b) => {
    if (Math.abs(a) % 9 != Math.abs(b) % 9) {
      return Math.abs(a) % 9 - Math.abs(b) % 9;
    } else {
      return nums.indexOf(a) - nums.indexOf(b);
    }
  });
  return nums;
}