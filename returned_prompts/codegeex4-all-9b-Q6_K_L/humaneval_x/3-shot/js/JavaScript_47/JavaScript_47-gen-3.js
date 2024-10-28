  l.sort((a, b) => a - b);
  var n = l.length;
  var m = n % 2;
  if (m == 1) {
    return l[Math.floor(n / 2)];
  } else {
    return (l[n / 2 - 1] + l[n / 2]) / 2.0;
  }
}