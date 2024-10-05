  let count = 0;
  for (let i = 1; i < n; i++) {
    if ((i % 11 == 0 || i % 13 == 0)) {
      count += (i.toString()).split('').filter(x => x == '7').length;
    }
  }
  return count;
}