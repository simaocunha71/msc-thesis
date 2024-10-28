const isHappy = (s) => {
  if (s.length < 3) return false
  const arr = s.split('')
  for (let i = 0; i < arr.length - 2; i++) {
    if (arr[i] === arr[i + 1] && arr[i + 1] === arr[i + 2]) return false
  }
  return true
}

