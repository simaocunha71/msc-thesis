  let closest = { min: Number.MAX_VALUE, pair: null };
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let distance = Math.abs(numbers[i] - numbers[j]);
      if (distance < closest.min) {
        closest.min = distance;
        closest.pair = [numbers[i], numbers[j]];
      }
    }
  }
  return closest.pair.sort((a, b) => a - b);
}