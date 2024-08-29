  let sum = 0;
  for (const n of numbers) {
    sum += Math.abs(n);
  }
  let mean = mean(numbers);
  return sum / numbers.length;
}



