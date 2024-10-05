  let counts = {};
  for (let num of lst) {
    counts[num] = (counts[num] || 0) + 1;
  }
  for (let num of lst) {
    if (counts[num] >= num) {
      return num;
    }
  }
  return -1;
}



