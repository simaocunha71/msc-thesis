  let counts = {};
  for (let num of lst) {
    counts[num] = (counts[num] || 0) + 1;
  }
  for (let i = lst.length; i > 0; i--) {
    if (counts[i]) return i;
  }
  return -1;
}



