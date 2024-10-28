const fixSpaces = (text) => {
  return text.replace(/ +/g, (match, index) => {
    if (match.length > 1) {
      return '-'
    }
    return '_'
  })
}
