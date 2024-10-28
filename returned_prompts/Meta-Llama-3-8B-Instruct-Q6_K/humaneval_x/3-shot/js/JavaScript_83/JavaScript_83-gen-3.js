  let count = 0;
  for (let i = 10**(n-1); i < 10**n; i++) {
    if (i.toString().startsWith('1') || i.toString().endsWith('1')) {
      count++;
    }
  }
  return count;
}