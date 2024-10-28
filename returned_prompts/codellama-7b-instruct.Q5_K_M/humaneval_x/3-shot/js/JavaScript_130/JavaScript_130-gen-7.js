  if (n == 0) {
    return [1];
  }

  var sequence = [1, 3, 2];
  if (n % 2 == 0) {
    for (var i = 3; i <= n; i++) {
      sequence[i] = sequence[i - 2] + sequence[i - 1] + sequence[i + 1];
    }
  } else {
    for (var i = 3; i <= n; i++) {
      sequence[i] = sequence[i - 1] + sequence[i - 2] + sequence[i + 1];
    }
  }

  return sequence;
}



