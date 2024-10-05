const tri = (n) => {
  const sequence = [1, 3]
  for (let i = 2; i <= n; i++) {
    if (i % 2 === 0) {
      sequence.push(sequence[i - 1] + sequence[i - 2])
    } else {
      sequence.push(sequence[i - 1] + sequence[i - 2] + sequence[i + 1])
    }
  }
  return sequence
}
