  return s0.split('').sort().join('') === s1.split('').sort().join('');
}
// or
const sameChars = (s0, s1) => {
  let s0_count = {};
  let s1_count = {};
  for (const c of s0) {
    s0_count[c] = (s0_count[c] || 0) + 1;
  }
  for (const c of s1) {
    s1_count[c] = (s1_count[c] || 0) + 1;
  }
  return JSON.stringify(s0_count) === JSON.stringify(s1_count);
}
// or
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  let s0_count = {};
  let s1_count = {};
  for (const c of s0) {
    s0_count[c] = (s0_count[c] || 0) + 1;
  }
  for (const c of s1) {
    s1_count[c] = (s1_count[c] || 0) + 1;
  }
  for (const key in s0_count) {
    if (s0_count[key] !== s1_count[key]) return false;
  }
  return true;
}
// or
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  let s0_count = {};
  let s1_count = {};
  for (const c of s0) {
    s0_count[c] = (s0_count[c] || 0) + 1;
  }
  for (const c of s1) {
    s1_count[c] = (s1_count[c] || 0) + 1;
  }
  let s0_keys = Object.keys(s0_count);
  let s1_keys = Object.keys(s1_count);
  for (const key of s0_keys) {
    if (!s1_keys.includes(key) || s0_count[key] !== s1_count[key]) return false;
  }
  return true;
}
// or
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  let s0_count = {};
  let s1_count = {};
  for (const c of s0) {
    s0_count