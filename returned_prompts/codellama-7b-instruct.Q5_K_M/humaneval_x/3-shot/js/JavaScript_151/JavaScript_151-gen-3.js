  var result = 0;
  for (const n of lst) {
    if (Number.isInteger(n) && n >= 0) {
      result += n * n;
    }
  }
  return result;
}



