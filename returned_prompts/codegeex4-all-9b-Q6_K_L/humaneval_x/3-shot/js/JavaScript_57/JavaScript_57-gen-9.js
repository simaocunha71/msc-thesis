  var increasing = true;
  var decreasing = true;

  for (var i = 1; i < l.length; i++) {
    if (l[i] > l[i - 1]) {
      decreasing = false;
    } else if (l[i] < l[i - 1]) {
      increasing = false;
    }
    if (!increasing && !decreasing) {
      return false;
    }
  }

  return true;
}



