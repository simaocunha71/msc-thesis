
const nextSmallest = (lst) => {
  const sorted = lst.sort((a, b) => a - b)
  return sorted[1]
}

