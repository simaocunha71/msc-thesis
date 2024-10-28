  let count = new Array(Math.max(...lst) + 1).fill(0);
  for (let num of lst) count[num]++;
  for (let i = count.length - 1; i >= 1; i--) {
    if (count[i] >= i) return i;
  }
  return -1;
}



