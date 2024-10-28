  var x = 0;
  var prev = 0;
  var n = xs.length;
  var threshold = 1e-6;

  while (Math.abs(poly(xs, x)) > threshold) {
    prev = x;
    x = prev - poly(xs, prev) / poly(xs, prev + threshold);
  }
  return x;
}



