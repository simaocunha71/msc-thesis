const countDistinctCharacters = (string) => {
  const characters = string.split('').map(char => char.toLowerCase())
  return [...new Set(characters)].length
}

