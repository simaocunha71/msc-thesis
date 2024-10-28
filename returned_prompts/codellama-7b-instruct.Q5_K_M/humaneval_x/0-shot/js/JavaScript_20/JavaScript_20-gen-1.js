
const findClosestElements = (numbers) => {
  const sorted = numbers.sort((a, b) => a - b)
  let closest = []
  for (let i = 0; i < numbers.length - 1; i++) {
    if (sorted[i + 1] - sorted[i] == 1) {
      closest.push(sorted[i])
      closest.push(sorted[i + 1])
    }
  }
  return closest
}

