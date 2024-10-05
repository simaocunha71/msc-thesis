  let count = 0;
  for (let i = 11; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      count += (i + '').replace(/7/g, '').length < (i + '').length ? 1 : 0;
    }
  }
  for (let i = 14; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      count += (i + '').replace(/7/g, '').length < (i + '').length ? 1 : 0;
    }
  }
  return count;
}