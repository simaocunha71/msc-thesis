
const multiply = (a, b) => {
  const aUnit = a % 10;
  const bUnit = b % 10;
  const aRemainder = (a - aUnit) / 10;
  const bRemainder = (b - bUnit) / 10;
  const product = aUnit * bUnit;
  const result = product + multiply(aRemainder, bRemainder);
  return result;
};

console.log(multiply(148, 412)); // 16
console.log(multiply(19, 28)); // 72
console.log(multiply(2020, 1851)); // 0
console.log(multiply(14,-15)); // 20
