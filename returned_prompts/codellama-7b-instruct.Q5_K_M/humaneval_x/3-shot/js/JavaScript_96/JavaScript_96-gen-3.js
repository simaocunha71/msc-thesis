  var result = [];
  for (var i = 2; i < n; i++) {
    var is_prime = true;
    for (var j = 2; j < i; j++) {
      if (i % j == 0) {
        is_prime = false;
        break;
      }
    }
    if (is_prime) {
      result.push(i);
    }
  }
  return result;
}



