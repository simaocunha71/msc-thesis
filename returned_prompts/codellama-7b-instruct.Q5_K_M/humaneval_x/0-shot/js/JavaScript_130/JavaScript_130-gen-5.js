  let sequence = [0, 1, 3];
  let i = 1;

  while (i <= n) {
    if (i % 2 === 0) {
      sequence.push(sequence[i - 1] + sequence[i - 2] / 2);
    } else {
      sequence.push(sequence[i - 1] + sequence[i - 2] + sequence[i + 1]);
    }
    i++;
  }
  return sequence;
};

