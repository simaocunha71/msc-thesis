  let fibs = [0, 0, 2];
  while (fibs.length <= n) {
    fibs.push(fibs[fibs.length - 1] + fibs[fibs.length - 2] + fibs[fibs.length - 3]);
  }
  return fibs[n];
}



