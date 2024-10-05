  return Array.from(s0).sort().join('') === Array.from(s1).sort().join('');
}
// Or
const sameChars = (s0, s1) => {
  return JSON.stringify(s0.split('').sort()) === JSON.stringify(s1.split('').sort());
}
// Or
const sameChars = (s0, s1) => {
  return new Set(s0).size === new Set(s1).size && Array.from(new Set(s0)).sort().join('') === Array.from(new Set(s1)).sort().join('');
}