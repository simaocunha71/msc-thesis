  let counts = {};
  let max_count = 0;

  for (let i = 0; i < lst.length; i++) {
    let num = lst[i];
    if (num in counts) {
      counts[num] += 1;
    } else {
      counts[num] = 1;
    }
    if (counts[num] > max_count) {
      max_count = counts[num];
    }
  }

  for (let num in counts) {
    if (counts[num] >= Number(num)) {
      return Number(num);
    }
  }

  return -1;
}



