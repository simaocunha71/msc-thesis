const removeDuplicates = (numbers) => {
  const seen = new Set()
  const unique = []
  numbers.forEach((number) => {
    if (!seen.has(number)) {
      unique.push(number)
      seen.add(number)
    }
  })
  return unique
}

