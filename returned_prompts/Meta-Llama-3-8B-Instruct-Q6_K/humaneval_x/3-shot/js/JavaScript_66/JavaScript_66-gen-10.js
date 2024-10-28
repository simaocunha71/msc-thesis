  let sum = 0;
  for (let c of s) {
    if (c.toUpperCase() !== c) {
      sum += c.charCodeAt(0);
    }
  }
  return sum;
}
// or
const digitSum = (s) => {
  return s.replace(/[^A-Z]/g, '').split('').map(c => c.charCodeAt(0)).reduce((a, b) => a + b, 0);
}