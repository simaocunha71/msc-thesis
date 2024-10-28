const circularShift = (x, shift) => {
  const str = x.toString()
  const len = str.length
  const shifted = (len + shift) % len
  return str.substr(shifted, len) + str.substr(0, shifted)
}

