  if (xs.length % 2 != 0 || xs.length == 0) {
    throw new Error('Cant find zero of polynomial with odd number of coefficients');
  }
  var max_coeff = Math.max(...xs);
  var x = 0;
  var step = 0.01;
  while (poly(xs, x) != 0) {
    var last_x = x;
    x = x - poly(xs, x) / poly(xs, last_x);
    step = x - last_x;
  }
  return x;
}



