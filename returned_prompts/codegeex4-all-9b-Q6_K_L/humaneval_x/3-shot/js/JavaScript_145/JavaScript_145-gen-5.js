  return nums.sort((a, b) => {
    if (a < 0) {
      a = -a;
    }
    if (b < 0) {
      b = -b;
    }
    let a_sum = 0;
    let b_sum = 0;
    while (a != 0) {
      a_sum += a % 10;
      a = Math.floor(a / 10);
    }
    while (b != 0) {
      b_sum += b % 10;
      b = Math.floor(b / 10);
    }
    if (a_sum == b_sum) {
      return nums.indexOf(a) - nums.indexOf(b);
    }
    return a_sum - b_sum;
  });
}