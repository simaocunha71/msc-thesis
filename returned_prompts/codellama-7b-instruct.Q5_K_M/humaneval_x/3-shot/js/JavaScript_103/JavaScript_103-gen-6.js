  if (n > m) return -1;

  var avg = (n + m) / 2;
  var rounded = Math.round(avg);
  var binary = rounded.toString(2);
  return binary;
}



