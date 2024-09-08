  let count = 0;
  for (const n of arr) {
    let digits = String(Math.abs(n)).split('').map(d => +d);
    if (digits.reduce((a, b) => a + b, 0) > 0) {
      count += 1;
    }
  }
  return count;
}



