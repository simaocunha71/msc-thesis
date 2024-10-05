

  const checkNumber = (x, n) => {
    let result = Math.pow(n, Math.log(x) / Math.log(n));
    return result === x;
  }
  return checkNumber(x, n);
}

