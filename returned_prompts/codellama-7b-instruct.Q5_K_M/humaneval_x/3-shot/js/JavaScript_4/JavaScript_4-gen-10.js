  const mean = meanOfNumbers(numbers);
  const deviations = numbers.map((x) => Math.abs(x - mean));
  return meanOfNumbers(deviations);
}



