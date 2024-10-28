  let fibs = [2, 3, 5, 13, 89];
  let index = 0;

  while (index < n) {
    let nextFib = fibs[index] + fibs[index + 1];
    fibs.push(nextFib);
    index += 1;
  }

  return fibs[n];
}



