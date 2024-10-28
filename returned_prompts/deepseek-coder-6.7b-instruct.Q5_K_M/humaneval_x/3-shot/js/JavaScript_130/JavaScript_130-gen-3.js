  let sequence = [1, 3, 2];
  if (n <= 2) {
    return sequence.slice(0, n + 1);
  }
  for (let i = 3; i <= n; i++) {
    sequence[i] = sequence[i - 1] + sequence[i - 2] + sequence[i - 3];
  }
  return sequence;
}



