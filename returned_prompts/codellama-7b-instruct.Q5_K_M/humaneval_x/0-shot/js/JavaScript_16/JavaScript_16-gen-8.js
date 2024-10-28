const countDistinctCharacters = (string) => {
  const stringLowerCase = string.toLowerCase()
  const distinctCharacters = new Set()
  for (const character of stringLowerCase) {
    distinctCharacters.add(character)
  }
  return distinctCharacters.size
}
