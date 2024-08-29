  const fibs = [0, 1];
  for (let i = 2; fibs[i] < Math.pow(10, 10); i++) {
    fibs.push(fibs[i - 1] + fibs[i - 2]);
    if (fibs[i] % 1 === 0) {
      continue;
    }
    for (let j = 2; j * j <= fibs[i]; j++) {
      if (fibs[i] % j === 0) {
        break;
      }
      if (j * j > fibs[i]) {
        return fibs[i];
      }
    }
  }
  return -1;
}



