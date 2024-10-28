  let count = 0;

  for (let i = 1; i <= n; i++) {
    if (i.toString().startsWith('1') || i.toString().endsWith('1')) {
      count++;
    }
  }

  return count;
}