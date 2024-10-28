const vowelsCount = (s) => {
  let count = 0
  for (let i = 0; i < s.length; i++) {
    if (s[i] === 'a' || s[i] === 'e' || s[i] === 'i' || s[i] === 'o' || s[i] === 'u' || s[i] === 'y') {
      count++
    }
  }
  return count
}

B:
const vowelsCount = (s) => {
  let count = 0
  for (const char of s) {
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u' || char === 'y') {
      count++
    }
  }
  return count
}

C:
const vowelsCount = (s) => {
  let count = 0
  s.split('').forEach(char => {
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u' || char === 'y') {
      count++
    }
  })
  return count
}