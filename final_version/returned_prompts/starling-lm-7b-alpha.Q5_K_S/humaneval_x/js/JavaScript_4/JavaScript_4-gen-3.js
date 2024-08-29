  let sum = 0;
  let mean = 0;

  for (const number of numbers) {
    sum += Math.abs(number);
    mean += number;
  }

  mean /= numbers.length;

  return sum / numbers.length - mean;
}



