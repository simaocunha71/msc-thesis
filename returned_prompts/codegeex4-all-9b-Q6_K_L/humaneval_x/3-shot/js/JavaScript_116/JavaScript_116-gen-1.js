  arr.sort((a, b) => {
    const a_ones = a.toString(2).split('1').length - 1;
    const b_ones = b.toString(2).split('1').length - 1;
    if (a_ones < b_ones) {
      return -1;
    } else if (a_ones > b_ones) {
      return 1;
    } else if (a < b) {
      return -1;
    } else if (a > b) {
      return 1;
    } else {
      return 0;
    }
  });
  return arr;
}