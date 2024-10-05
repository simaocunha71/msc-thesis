const common = (l1, l2) => {
  let result = []
  l1.forEach(i => {
    if (l2.includes(i)) {
      result.push(i)
    }
  })
  return result.sort((a, b) => a - b)
}

