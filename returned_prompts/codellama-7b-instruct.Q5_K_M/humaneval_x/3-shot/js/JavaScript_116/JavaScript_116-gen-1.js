  arr.sort((a, b) => {
    const a_ones = a.toString(2).split('1').length - 1;
    const b_ones = b.toString(2).split('1').length - 1;
    if (a_ones !== b_ones) {
      return a_ones - b_ones;
    } else {
      return a - b;
    }
  });
  return arr;
}



