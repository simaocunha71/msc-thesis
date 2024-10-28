  let result = true
  const keys = Object.keys(dict)
  for (let i = 0; i < keys.length; i++) {
    const key = keys[i]
    if (typeof key !== 'string') {
      return false
    }
    const keyLower = key.toLowerCase()
    const keyUpper = key.toUpperCase()
    if (keyLower === keyUpper) {
      continue
    }
    result = false
    break
  }
  return result
}
