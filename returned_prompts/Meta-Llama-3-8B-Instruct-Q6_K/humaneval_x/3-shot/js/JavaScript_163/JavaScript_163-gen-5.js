  let result = [];
  for (let i = a; i <= b; i++) {
    if (i % 2 === 0) {
      result.push(i);
    }
  }
  return result;
}
// or
const generateIntegers = (a, b) => {
  return Array.from({ length: Math.abs(b - a) + 1 }, (_, i) => a + i).filter(i => i % 2 === 0).sort((a, b) => a - b);
}