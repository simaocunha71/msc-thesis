const generateIntegers = (a, b) => {
  const result = [];
  for (let i = a; i <= b; i++) {
    if (i % 2 === 0) {
      result.push(i);
    }
  }
  return result;
};

// B:
const generateIntegers = (a, b) => {
  return Array.from({ length: b - a + 1}, (_, i) => 2 * i + a).filter(i => i % 2 === 0);
};

// C:
const generateIntegers = (a, b) => {
  return Array.from(Array(b - a + 1), (_, i) => 2 * i + a).filter(i => i % 2 === 0);
};
