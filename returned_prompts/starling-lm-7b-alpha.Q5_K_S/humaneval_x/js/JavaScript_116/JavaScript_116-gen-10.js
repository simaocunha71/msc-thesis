  const compare = (a, b) => {
    const [ones_a, val_a] = [getOnes(a), a];
    const [ones_b, val_b] = [getOnes(b), b];

    if (ones_a < ones_b) {
      return -1;
    } else if (ones_a > ones_b) {
      return 1;
    } else if (val_a < val_b) {
      return -1;
    } else if (val_a > val_b) {
      return 1;
    } else {
      return 0;
    }
  };

  return [...arr].sort(compare);
}

const getOnes = (num) => {
  const bin_str = num.toString(2);
  return bin_str.match(/[01]/g).length;
}



