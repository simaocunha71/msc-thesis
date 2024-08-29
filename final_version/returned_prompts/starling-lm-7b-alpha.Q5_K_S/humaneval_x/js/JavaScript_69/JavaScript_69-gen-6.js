  const numCount = (n) => lst.filter(x => x === n).length;
  const max = Math.max(...lst);
  let result = -1;
  for (let i = max; i >= 1; i--) {
    if (numCount(i) >= i) {
      result = i;
      break;
    }
  }
  return result;
}



