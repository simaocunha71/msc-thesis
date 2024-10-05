  var sum = 0.0;

  var mean = numbers.reduce((a, b) => a + b) / numbers.length;

  for (const n of numbers) {
    sum += Math.abs(n - mean);
  }

  return sum / numbers.length;
}



