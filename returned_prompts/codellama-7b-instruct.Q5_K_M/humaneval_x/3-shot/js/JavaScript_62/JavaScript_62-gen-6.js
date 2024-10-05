  var result = [];
  var prev_x = 0;
  var prev_x_pow = 1;
  for (var i = 0; i < xs.length; i++) {
    var x = xs[i];
    var x_pow = 1;
    if (i > 0) {
      x_pow = prev_x_pow * i;
    }
    var derivative_x = x * x_pow;
    result.push(derivative_x);
    prev_x = x;
    prev_x_pow = x_pow;
  }
  return result;
}



