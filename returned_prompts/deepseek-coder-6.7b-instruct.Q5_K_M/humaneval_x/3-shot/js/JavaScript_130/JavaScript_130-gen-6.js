  var seq = [3];
  if (n > 0) seq.push(2);
  if (n > 1) seq.push(1);
  if (n > 2) {
    for (var i = 3; i <= n; i++) {
      if (i % 2 === 0) {
        seq.push(1 + i / 2);
      } else {
        seq.push(seq[i - 1] + seq[i - 2] + seq[i - 3]);
      }
    }
  }
  return seq;
}



