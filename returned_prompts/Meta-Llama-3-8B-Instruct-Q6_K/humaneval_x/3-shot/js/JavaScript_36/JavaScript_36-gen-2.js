  let count = 0;
  for (let i = 11; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      count += (i.toString()).split('').filter(x => x == '7').length;
    }
  }
  for (let i = 7; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      count += (i.toString()).split('').filter(x => x == '7').length;
    }
  }
  return count;
}