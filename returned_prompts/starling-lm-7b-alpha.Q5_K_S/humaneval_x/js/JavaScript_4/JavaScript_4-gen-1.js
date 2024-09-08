  const mean = (numbers) => {
    let sum = 0;
    for (const n of numbers) {
      sum += n;
    }
    return sum / numbers.length;
  }
  const absoluteDifference = (n, mean) => Math.abs(n - mean);
  const average = (numbers) => numbers.reduce((sum, n) => sum + n) / numbers.length;

  const sum = numbers.map(absoluteDifference).reduce(average);

  return sum;
}



