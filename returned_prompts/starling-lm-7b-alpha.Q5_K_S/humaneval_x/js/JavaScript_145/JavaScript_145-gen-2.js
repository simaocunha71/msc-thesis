  return nums.sort((a, b) => {
    let sum_a = 0;
    let sum_b = 0;

    while (a > 0) {
      sum_a += a % 10;
      a = Math.floor(a / 10);
    }

    while (b > 0) {
      sum_b += b % 10;
      b = Math.floor(b / 10);
    }

    if (sum_a === sum_b) {
      return nums.indexOf(a) - nums.indexOf(b);
    } else {
      return sum_a - sum_b;
    }
  });
}



