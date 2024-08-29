  let count = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i != j && Math.abs(i - j) % (n + 1) == 0) {
        count += 1;
      }
    }
  }

  return count;
}



