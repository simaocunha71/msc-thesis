  l.sort((a, b) => a - b);
  let n = l.length;
  if (n % 2 == 0) {
    let mid1 = l[n / 2 - 1];
    let mid2 = l[n / 2];
    return (mid1 + mid2) / 2;
  } else {
    return l[n / 2];
  }
}