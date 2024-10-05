const rescaleToUnit = numbers => numbers
  .sort((a, b) => a - b)
  .map((number, index, numbers) => index === 0
    ? 0
    : index === numbers.length - 1
      ? 1
      : (number - numbers[index - 1]) / (numbers[numbers.length - 1] - numbers[index - 1])
  );

