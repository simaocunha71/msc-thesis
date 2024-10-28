const isHappy = (s) => {
  return s.length >= 3 && s.split('').reduce((acc, cur, i, arr) => {
    if (i < 2) return acc
    if (cur === arr[i - 1] && cur === arr[i - 2]) return false
    return acc
  }, true)
}
