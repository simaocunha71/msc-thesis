  l.sort((a, b) => a - b);
  let n = l.length;
  if (n % 2 == 0) {
    let mid = Math.floor(n / 2);
    return (l[mid - 1] + l[mid]) / 2;
  } else {
    return l[Math.floor(n / 2)];
  }
}