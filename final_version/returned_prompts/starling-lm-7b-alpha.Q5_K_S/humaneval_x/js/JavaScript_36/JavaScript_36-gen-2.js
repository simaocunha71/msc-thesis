  let count = 0;
  for (let i = 1; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      if (i.toString().includes("7")) {
        count += 1;
      }
    }
  }
  return count;
}



