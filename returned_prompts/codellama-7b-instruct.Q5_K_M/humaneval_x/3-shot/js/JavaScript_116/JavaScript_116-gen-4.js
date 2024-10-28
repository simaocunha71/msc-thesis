  return arr.sort((a, b) => {
    const a_ones = (a.toString(2).match(/1/g) || []).length;
    const b_ones = (b.toString(2).match(/1/g) || []).length;

    if (a_ones != b_ones) {
      return a_ones - b_ones;
    } else {
      return a - b;
    }
  });
}



