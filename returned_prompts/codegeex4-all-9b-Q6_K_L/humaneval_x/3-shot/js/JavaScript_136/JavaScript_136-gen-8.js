  var pos = null;
  var neg = null;

  for (const i of lst) {
    if (i > 0 && (pos == null || i < pos)) {
      pos = i;
    } else if (i < 0 && (neg == null || i > neg)) {
      neg = i;
    }
  }

  return [neg, pos];
}