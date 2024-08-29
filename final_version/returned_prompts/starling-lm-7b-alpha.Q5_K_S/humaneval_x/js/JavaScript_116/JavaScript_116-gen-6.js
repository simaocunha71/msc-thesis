  let array = arr.slice(0);
  array.sort((a, b) => {
    let a_ones = a.toString(2).split('').filter(v => v === '1').length;
    let b_ones = b.toString(2).split('').filter(v => v === '1').length;
    if (a_ones === b_ones) {
      return a - b;
    }
    return a_ones - b_ones;
  });
  return array;
}



