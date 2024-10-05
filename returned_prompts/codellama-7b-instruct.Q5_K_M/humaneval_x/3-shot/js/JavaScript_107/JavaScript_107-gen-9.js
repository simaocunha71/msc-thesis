  var result = [0, 0];
  var list = [];

  for (var i = 1; i <= n; i++) {
    list.push(i);
  }

  for (var i = 0; i < list.length; i++) {
    var num = list[i];
    if (num == num.toString().split('').reverse().join('')) {
      if (num % 2 == 0) {
        result[0] += 1;
      } else {
        result[1] += 1;
      }
    }
  }

  return result;
}



