  let sequence = [3];
  for (let i = 1; i < n; i++) {
    let next = 0;
    if (i % 2 === 0) {
      next = 1 + i / 2;
    } else {
      let prev1 = sequence[sequence.length - 1];
      let prev2 = sequence[sequence.length - 2];
      next = prev1 + prev2 + (i > 2 ? sequence[sequence.length - 3] : 0);
    }
    sequence.push(next);
  }
  return sequence;
}
