  let max = -1;
  for (let i = 1; i <= Math.max(...lst); i++) {
    if (lst.filter(j => j === i).length >= i) {
      max = i;
    }
  }
  return max;
}