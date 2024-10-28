  let frequencies = {};
  for (let n of lst) {
    if (n in frequencies) {
      frequencies[n] += 1;
    } else {
      frequencies[n] = 1;
    }
  }

  let max = -1;
  for (let n in frequencies) {
    if (frequencies[n] >= n && n > max) {
      max = n;
    }
  }

  return max;
}



