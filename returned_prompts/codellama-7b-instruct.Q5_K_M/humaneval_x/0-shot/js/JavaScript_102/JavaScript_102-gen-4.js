const chooseNum = (x, y) => {
  const evens = [...Array(y - x + 1)].map((_, i) => i * 2 + x).filter(v => v >= x && v <= y);
  return evens[0] || -1;
};

// OR
const chooseNum = (x, y) => {
  for (let i = x; i <= y; i += 2) return i;
  return -1;
};
