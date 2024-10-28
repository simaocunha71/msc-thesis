const rollingMax = (numbers) => {
  return numbers.map((n, i, a) => Math.max(n, ...a.slice(i)))
}
