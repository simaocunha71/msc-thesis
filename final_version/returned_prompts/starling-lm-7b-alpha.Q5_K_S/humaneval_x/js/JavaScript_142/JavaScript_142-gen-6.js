  for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) {
      lst[i] *= lst[i];
    } else if (i % 4 === 0 && i % 3 !== 0) {
      lst[i] *= lst[i] * lst[i];
    }
  }
  return lst.reduce((a, b) => a + b, 0);
}



