  var result = false;
  if (a < 100) {
    for (let i = 2; i < 10; i++) {
      if (a % i == 0) {
        var j = 0;
        while (a % i == 0) {
          a = a / i;
          j += 1;
        }
        if (j == 3) {
          result = true;
          break;
        }
      }
    }
  }
  return result;
}



