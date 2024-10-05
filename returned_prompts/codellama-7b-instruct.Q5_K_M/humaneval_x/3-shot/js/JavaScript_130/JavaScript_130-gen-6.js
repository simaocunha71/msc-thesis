  let sequence = [1, 1, 2];
  for (let i = 3; i <= n; i++) {
    if (i % 2 === 0) {
      sequence.push(1 + i / 2);
    } else {
      sequence.push(sequence[i - 1] + sequence[i - 2] + sequence[i + 1]);
    }
  }

  return sequence;
}



