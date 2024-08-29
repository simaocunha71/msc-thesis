  let count = {};

  for (const i of lst) {
    if (count[i] === undefined) {
      count[i] = 0;
    }
    count[i] += 1;
  }

  for (const i of lst) {
    if (count[i] >= i) {
      return i;
    }
  }

  return -1;
}



