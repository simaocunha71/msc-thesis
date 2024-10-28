  var prime_array = [];

  for (var i = 2; i < n; i++) {
    var flag = true;
    for (var j = 2; j < i; j++) {
      if (i % j == 0) {
        flag = false;
        break;
      }
    }
    if (flag) {
      prime_array.push(i);
    }
  }

  return prime_array;
}



