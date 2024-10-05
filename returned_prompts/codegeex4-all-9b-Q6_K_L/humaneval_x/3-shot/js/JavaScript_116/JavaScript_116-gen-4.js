  return arr.sort((a, b) => {
    let ones_a = a.toString(2).split('1').length - 1;
    let ones_b = b.toString(2).split('1').length - 1;
    if (ones_a == ones_b) {
      return a - b;
    } else {
      return ones_a - ones_b;
    }
  });
}



