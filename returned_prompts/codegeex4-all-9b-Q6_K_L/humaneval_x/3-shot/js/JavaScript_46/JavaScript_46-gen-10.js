  var fibs = [0, 0, 2, 0];

  for (var i = 4; i <= n; i++) {
    fibs.push(fibs[i-1] + fibs[i-2] + fibs[i-3] + fibs[i-4]);
  }

  return fibs[n];
}