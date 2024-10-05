const isHappy = (s) => {
  if (s.length < 3) return false
  const subs = s.split('')
  for (let i = 0; i < subs.length - 2; i++) {
    if (subs[i] === subs[i + 1] && subs[i + 1] === subs[i + 2]) {
      return false
    }
  }
  return true
}
