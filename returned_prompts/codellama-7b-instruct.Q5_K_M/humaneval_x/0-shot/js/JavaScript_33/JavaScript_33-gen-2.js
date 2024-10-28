const sortThird = (l) => {
  const sorted = l.map((val, i) => {
    if (i % 3 === 0) {
      return l.filter((_, j) => j % 3 === 0).sort((a, b) => a - b)
    }
    return val
  })
  return sorted
}

