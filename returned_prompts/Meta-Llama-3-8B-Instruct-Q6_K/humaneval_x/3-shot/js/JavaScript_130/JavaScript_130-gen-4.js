  let sequence = [1, 3];
  for (let i = 2; i < n; i++) {
    if (i % 2 === 0) {
      sequence.push(1 + i / 2);
    } else {
      let last = sequence[sequence.length - 1];
      let secondLast = sequence[sequence.length - 2];
      let prev = sequence[sequence.length - 3];
      sequence.push(last + secondLast + prev);
    }
  }
  return sequence;
}