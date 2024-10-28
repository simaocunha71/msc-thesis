  let count = 0;
  for (let i = 0; i < n; i++) {
    let divisible = i % 11 == 0 || i % 13 == 0;
    if (divisible) {
      let str = i.toString();
      for (const c of str) {
        if (c == '7') {
          count += 1;
        }
      }
    }
  }
  return count;
}

