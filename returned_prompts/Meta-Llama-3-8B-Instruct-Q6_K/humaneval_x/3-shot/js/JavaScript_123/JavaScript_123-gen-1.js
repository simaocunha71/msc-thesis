  const sequence = [n];
  while (n !== 1) {
    if (n % 2 === 0) {
      n = Math.floor(n / 2);
    } else {
      n = n * 3 + 1;
    }
    sequence.push(n);
  }
  return sequence.filter(x => x % 2 !== 0).sort((a, b) => a - b);
}*/



