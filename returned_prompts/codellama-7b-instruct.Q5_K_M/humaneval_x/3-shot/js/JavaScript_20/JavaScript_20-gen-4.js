  var closest_pair = [numbers[0], numbers[0]];
  var closest_distance = Math.abs(closest_pair[0] - closest_pair[1]);

  for (var i = 0; i < numbers.length; i++) {
    for (var j = i + 1; j < numbers.length; j++) {
      var current_distance = Math.abs(numbers[i] - numbers[j]);
      if (current_distance < closest_distance) {
        closest_pair = [numbers[i], numbers[j]];
        closest_distance = current_distance;
      }
    }
  }
  return closest_pair;
}



