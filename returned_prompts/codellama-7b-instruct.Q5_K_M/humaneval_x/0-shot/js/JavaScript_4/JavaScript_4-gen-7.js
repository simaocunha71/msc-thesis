const meanAbsoluteDeviation = (numbers) => {
const mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
return numbers.map((n) => Math.abs(n - mean)).reduce((a, b) => a + b, 0) / numbers.length;
};

