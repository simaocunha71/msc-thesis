const findMax = (words) => {
  words.sort((a, b) => b.length - a.length)
  return words[0]
}

