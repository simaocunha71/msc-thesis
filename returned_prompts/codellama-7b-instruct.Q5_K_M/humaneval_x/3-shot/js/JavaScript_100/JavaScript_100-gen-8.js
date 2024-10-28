  var result = [];

  for (var i = 0; i < n; i++) {
    var current_level = n;
    if (n % 2 == 0) {
      current_level += 1;
    }
    result.push(current_level);
    n = current_level;
  }

  return result;
}



