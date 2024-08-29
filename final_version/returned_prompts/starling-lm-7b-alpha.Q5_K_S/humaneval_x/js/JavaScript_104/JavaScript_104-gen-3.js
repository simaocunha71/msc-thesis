  let result = [];
  for (let i = 0; i < x.length; i++) {
    if (check(x[i])) {
      result.push(x[i]);
    }
  }
  result.sort((a, b) => a - b);
  return result;

  function check(n) {
    while (n > 0) {
      let d = n % 10;
      if (d % 2 == 0) {
        return false;
      }
      n = Math.floor(n / 10);
    }
    return true;
  }
}



