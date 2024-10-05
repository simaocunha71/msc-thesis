  var closest = [];

  for (var i = 0; i < numbers.length; i++) {
    for (var j = i + 1; j < numbers.length; j++) {
      if (Math.abs(numbers[i] - numbers[j]) < Math.abs(closest[0] - closest[1])) {
        closest = [numbers[i], numbers[j]];
      }
    }
  }

  return closest;
}



