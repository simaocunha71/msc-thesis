  var copy = [...array];
  var sum = copy[0] + copy[copy.length - 1];
  if (sum % 2 == 0) {
    copy.sort((a, b) => b - a);
  } else {
    copy.sort((a, b) => a - b);
  }
  return copy;
}

