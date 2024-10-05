const multiply = (a, b) => {
  return Math.abs(a % 10) * Math.abs(b % 10);
};

multiply(148, 412) // 16
multiply(19, 28) // 72
multiply(2020, 1851) // 0
multiply(14,-15) // 20
