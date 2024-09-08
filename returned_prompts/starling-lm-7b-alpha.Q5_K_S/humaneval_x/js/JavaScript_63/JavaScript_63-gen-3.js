  if (n == 0 || n == 1) {
    return 0;
  } else if (n == 2) {
    return 1;
  }

  var fibs = [0, 0, 1];
  while (fibs.length <= n) {
    fibs.push(fibs[fibs.length - 1] + fibs[fibs.length - 2] + fibs[fibs.length - 3]);
  }

  return fibs[fibs.length - 1];
}



