  return arr.sort((a, b) => {
    let a_binary = a.toString(2);
    let b_binary = b.toString(2);
    let a_ones = a_binary.split('1').length - 1;
    let b_ones = b_binary.split('1').length - 1;

    if (a_ones !== b_ones) {
      return a_ones - b_ones;
    } else {
      return a - b;
    }
  });
};



