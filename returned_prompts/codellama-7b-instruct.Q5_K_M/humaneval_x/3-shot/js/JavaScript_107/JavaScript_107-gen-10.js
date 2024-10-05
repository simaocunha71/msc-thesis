  var result = [];
  for (var i = 1; i <= n; i++) {
    var num = i.toString();
    if (num == num.split('').reverse().join('')) {
      if (i % 2 == 0) {
        result[0] = result[0] ? result[0] + 1 : 1;
      } else {
        result[1] = result[1] ? result[1] + 1 : 1;
      }
    }
  }
  return result;
}



