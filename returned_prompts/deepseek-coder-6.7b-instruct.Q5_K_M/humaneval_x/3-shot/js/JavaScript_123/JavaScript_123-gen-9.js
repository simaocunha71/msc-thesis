  let collatz = [n];
  let next = n;
  while (next != 1){
    next = next % 2 == 0 ? next / 2 : next * 3 + 1;
    if (next % 2 != 0) collatz.push(next);
  }
  return collatz.sort((a, b) => a - b);
}



