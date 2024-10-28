  var closest = [undefined, undefined];
  var closest_distance = Infinity;

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let distance = Math.abs(numbers[i] - numbers[j]);
      if (distance < closest_distance) {
        closest_distance = distance;
        closest = [numbers[i], numbers[j]];
      }
    }
  }

  return closest;
}



