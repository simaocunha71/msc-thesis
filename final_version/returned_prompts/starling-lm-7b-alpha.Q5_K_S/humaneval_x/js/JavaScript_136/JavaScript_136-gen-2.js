  let neg = null;
  let pos = null;
  for (const n of lst) {
    if (n < 0 && (neg === null || neg < n)) {
      neg = n;
    }
    if (n > 0 && (pos === null || pos > n)) {
      pos = n;
    }
  }
  return [neg, pos];
}



