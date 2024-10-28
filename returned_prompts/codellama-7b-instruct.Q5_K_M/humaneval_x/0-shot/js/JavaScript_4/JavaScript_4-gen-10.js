const mean = numbers.reduce((a, b) => a + b, 0) / numbers.length;
const deviations = numbers.map((x) => Math.abs(x - mean));
const sum = deviations.reduce((a, b) => a + b, 0);
return sum / numbers.length;
}
