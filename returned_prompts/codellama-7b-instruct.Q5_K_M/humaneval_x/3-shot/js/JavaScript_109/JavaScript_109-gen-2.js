  if (arr.length == 0) {
    return true;
  }

  var sorted = arr.sort((a, b) => a - b);

  for (let i = 0; i < sorted.length - 1; i++) {
    if (sorted[i] >= sorted[i + 1]) {
      return false;
    }
  }

  return true;
}



