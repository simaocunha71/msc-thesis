  return nums.sort((a, b) => {
    let sum_a = a.toString().split('').reduce((sum, digit) => sum + parseInt(digit), 0);
    let sum_b = b.toString().split('').reduce((sum, digit) => sum + parseInt(digit), 0);
    if (sum_a < sum_b) {
      return -1;
    } else if (sum_a > sum_b) {
      return 1;
    } else {
      return nums.indexOf(a) - nums.indexOf(b);
    }
  });
}



