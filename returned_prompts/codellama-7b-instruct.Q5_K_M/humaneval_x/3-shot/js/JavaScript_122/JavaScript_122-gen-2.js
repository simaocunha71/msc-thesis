  var sum = 0;
  for (var i = 0; i < k; i++) {
    var current = arr[i];
    if (current < 10 && current >= 0) {
      sum += current;
    } else if (current < 100 && current >= 10) {
      sum += current % 10 + current / 10;
    }
  }
  return sum;
}



