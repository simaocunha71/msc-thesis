  let count = 0;
  for (let i = 11; i < n; i += 11) {
    if (i.toString().includes('7')) {
      count++;
    }
  }
  for (let i = 13; i < n; i += 13) {
    if (i.toString().includes('7')) {
      count++;
    }
  }
  return count;
}