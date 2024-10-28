  return nums.sort((a, b) => {
    if (Math.abs(a) % 10 === Math.abs(b) % 10) {
      return nums.indexOf(a) - nums.indexOf(b);
    } else {
      return Math.abs(a) % 10 - Math.abs(b) % 10;
    }
  });
}