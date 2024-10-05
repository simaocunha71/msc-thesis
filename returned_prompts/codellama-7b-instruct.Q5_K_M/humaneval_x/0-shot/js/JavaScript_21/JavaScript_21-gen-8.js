const rescaleToUnit = (numbers) => {
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const range = max - min;
  return numbers.map(num => (num - min) / range);
}
