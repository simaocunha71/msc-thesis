const multiply = (a, b) => {
  const unitA = Math.abs(a) % 10;
  const unitB = Math.abs(b) % 10;
  return unitA * unitB;
}