const removeDuplicates = (numbers) => {
  const unique = []
  for (let number of numbers) {
    if (!unique.includes(number)) {
      unique.push(number)
    }
  }
  return unique
}

