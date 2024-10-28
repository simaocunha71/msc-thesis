  var x = 0;
  var y = poly(xs, x);
  var prev_x = 0;
  var prev_y = y;
  var step = 0.01;

  while (Math.abs(y) > 0.001) {
    x += step;
    y = poly(xs, x);
    var slope = (y - prev_y) / (x - prev_x);
    step = -y / slope;
    prev_x = x;
    prev_y = y;
  }
  return x;
}



