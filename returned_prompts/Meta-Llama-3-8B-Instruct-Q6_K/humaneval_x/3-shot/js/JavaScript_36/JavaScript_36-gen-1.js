  let count = 0;
  for (let i = 11; i < n; i += 11) {
    count += (i.toString().includes('7')) ? 1 : 0;
  }
  for (let i = 13; i < n; i += 13) {
    count += (i.toString().includes('7')) ? 1 : 0;
  }
  return count;
}