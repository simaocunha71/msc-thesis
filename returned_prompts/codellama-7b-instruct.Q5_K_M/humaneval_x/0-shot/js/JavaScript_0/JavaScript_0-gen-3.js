/* Check if in given list of numbers, are any two numbers closer to each other than
  given threshold.
  >>> hasCloseElements([1.0, 2.0, 3.0], 0.5)
  false
  >>> hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
  true
  */
const hasCloseElements = (numbers, threshold) => {
  const sorted = numbers.sort((a, b) => a - b);
  for (let i = 0; i < sorted.length - 1; i++) {
    const diff = sorted[i] - sorted[i + 1];
    if (diff < 0) {
      diff = Math.abs(diff);
    }
    if (diff < threshold) {
      return true;
    }
  }
  return false;
};

