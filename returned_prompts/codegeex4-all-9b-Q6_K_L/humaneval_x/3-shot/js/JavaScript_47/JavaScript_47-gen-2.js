  var sorted = l.sort((a, b) => a - b);
  var middle = Math.floor(sorted.length / 2);
  if (sorted.length % 2 == 0) {
    return (sorted[middle - 1] + sorted[middle]) / 2;
  } else {
    return sorted[middle];
  }
}



