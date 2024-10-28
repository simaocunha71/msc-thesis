  const max = Math.max(...lst);

  for (let i = 1; i <= max; i++) {
    if (lst.filter(x => x >= i).length >= i) {
      return i;
    }
  }

  return -1;
}



