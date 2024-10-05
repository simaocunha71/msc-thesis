  return arr.sort((a, b) => {
    if (a < 0) return 1;
    if (b < 0) return -1;
    let ones_a = a.toString(2).split('').filter(c => c === '1').length;
    let ones_b = b.toString(2).split('').filter(c => c === '1').length;
    if (ones_a !== ones_b) return ones_a - ones_b;
    return a - b;
  });
}