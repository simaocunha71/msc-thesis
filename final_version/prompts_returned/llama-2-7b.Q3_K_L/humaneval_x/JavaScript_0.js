/* Check if in given list of numbers, are any two numbers closer to each other than
  given threshold.
  >>> hasCloseElements([1.0, 2.0, 3.0], 0.5)
  false
  >>> hasCloseElements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
  true
  */
const hasCloseElements = (numbers, threshold) => {
  const distances = numbers.map((number) => Math.abs(number));
  
  for (let i = 1; i < distances.length - 2; i++) {
    // check if current distance is more than threshold
    if (distances[i] > threshold && distances[i + 1] >= threshold) return true;
  }
  
  return false;
};