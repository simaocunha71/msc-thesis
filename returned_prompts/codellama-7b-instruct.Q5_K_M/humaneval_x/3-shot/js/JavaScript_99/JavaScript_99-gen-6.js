  var n = Number(value);

  if (n % 1 === 0.5) {
    if (n > 0) {
      return n + 1;
    } else {
      return n - 1;
    }
  } else {
    return Math.round(n);
  }
}



