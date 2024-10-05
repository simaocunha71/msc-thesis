const findClosestElements = (numbers) => {
  let minDiff = Infinity;
  let result = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let diff = Math.abs(numbers[i] - numbers[j]);
      if (diff < minDiff) {
        minDiff = diff;
        result = [numbers[i], numbers[j]];
      }
    }
  }

  return result;
};

console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])); // (2.0, 2.2)
console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])); // (2.0, 2.0)