  let result = [];
  let sequence = [n];

  while (n !== 1) {
    if (n % 2 === 0) {
      n = Math.floor(n / 2);
    } else {
      n = n * 3 + 1;
    }
    if (!sequence.includes(n)) {
      sequence.push(n);
    }
  }

  for (let i = 0; i < sequence.length; i++) {
    if (sequence[i] % 2 !== 0) {
      result.push(sequence[i]);
    }
  }

  return result.sort((a, b) => a - b);
}