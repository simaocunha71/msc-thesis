const multiply = (a, b) => {
  return (a % 10) * (b % 10);
};
console.log(multiply(148, 412)); // 16
console.log(multiply(19, 28)); // 72
console.log(multiply(2020, 1851)); // 0
console.log(multiply(14, -15)); // 20