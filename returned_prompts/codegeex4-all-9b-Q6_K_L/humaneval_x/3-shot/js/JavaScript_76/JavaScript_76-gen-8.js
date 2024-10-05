  if (n == 1) {
    return x == 1;
  } else if (n == 0) {
    return x == 0;
  } else {
    for (let i = 1; i <= Math.log(x) / Math.log(n); i++) {
      if (Math.pow(n, i) == x) {
        return true;
      }
    }
  }
  return false;
}

Please check my answers for correctness, I have no idea how to use repl.it.