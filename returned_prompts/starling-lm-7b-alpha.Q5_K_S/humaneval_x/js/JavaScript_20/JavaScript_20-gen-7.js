  let min = Number.MAX_SAFE_INTEGER;
  let closest_elements = null;
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (Math.abs(numbers[i] - numbers[j]) < min) {
        min = Math.abs(numbers[i] - numbers[j]);
        closest_elements = [numbers[i], numbers[j]];
      }
    }
  }
  return closest_elements;
}



