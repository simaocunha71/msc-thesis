  let max = Math.max(...lst);
  let freq = lst.filter(x => x === max).length;
  for (let i = max; i >= 0; i--) {
    if (freq(lst, i) >= i) {
      return i;
    }
  }
  return -1;
}

function freq(lst, val) {
  return lst.reduce((acc, curr) => (curr === val) ? acc + 1 : acc, 0);
}



