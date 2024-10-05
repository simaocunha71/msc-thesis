const longest = (strings) => {
  if (!strings.length) return null
  return strings.reduce((longest, current) => {
    return current.length > longest.length ? current : longest
  }, strings[0])
}
