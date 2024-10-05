const largestSmallestIntegers = (lst) => {
  const negatives = lst.filter(num => num < 0).sort((a, b) => b - a)
  const positives = lst.filter(num => num > 0).sort((a, b) => a - b)
  return [negatives.length ? negatives[0] : null, positives.length ? positives[0] : null]
}