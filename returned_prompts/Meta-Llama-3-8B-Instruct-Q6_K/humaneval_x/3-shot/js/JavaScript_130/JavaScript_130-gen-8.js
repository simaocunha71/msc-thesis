  let sequence = [1, 3];
  for (let i = 2; i < n; i++) {
    let sum = 0;
    if (i % 2 === 0) {
      sum = 1 + i / 2;
    } else {
      sum = sequence[i - 1] + sequence[i - 2] + sequence[i - 3];
    }
    sequence.push(sum);
  }
  return sequence;
}