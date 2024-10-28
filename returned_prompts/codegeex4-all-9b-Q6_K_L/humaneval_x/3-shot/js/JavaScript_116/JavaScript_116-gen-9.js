  return arr.sort((a, b) => {
    let a_ones = (a >>> 0).toString(2).split('1').length - 1;
    let b_ones = (b >>> 0).toString(2).split('1').length - 1;
    return a_ones - b_ones || a - b;
  });
}