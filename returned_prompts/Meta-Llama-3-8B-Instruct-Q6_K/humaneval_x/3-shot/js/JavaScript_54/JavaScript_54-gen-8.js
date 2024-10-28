  return Array.from(new Set(s0.split(''))).join('') === Array.from(new Set(s1.split(''))).join('');
}
// or
const sameChars = (s0, s1) => {
  return s0.split('').sort().join('') === s1.split('').sort().join('');
}
// or
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  for (let c of s0) {
    if (s1.indexOf(c) === -1) return false;
  }
  return true;
}