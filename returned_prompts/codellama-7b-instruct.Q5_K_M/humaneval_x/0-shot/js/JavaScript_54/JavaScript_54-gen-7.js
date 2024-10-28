const sameChars = (s0, s1) => {
  // return s0.split('').sort().join('') === s1.split('').sort().join('')
  return [...s0].sort().join('') === [...s1].sort().join('')
}

