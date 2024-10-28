  return arr.sort((a, b) => {
    if (a < 0) {
      a = -a;
    }
    if (b < 0) {
      b = -b;
    }
    let a_ones = 0;
    let b_ones = 0;
    while (a > 0) {
      if (a % 2 == 1) {
        a_ones += 1;
      }
      a = Math.floor(a / 2);
    }
    while (b > 0) {
      if (b % 2 == 1) {
        b_ones += 1;
      }
      b = Math.floor(b / 2);
    }
    if (a_ones == b_ones) {
      return a - b;
    }
    return a_ones - b_ones;
  });
}