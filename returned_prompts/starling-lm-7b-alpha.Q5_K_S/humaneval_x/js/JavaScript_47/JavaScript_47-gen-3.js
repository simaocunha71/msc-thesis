  l.sort((a, b) => a - b);
  let n = l.length;
  if (n % 2 == 0) {
    return (l[n / 2 - 1] + l[n / 2]) / 2;
  } else {
    return l[Math.floor(n / 2)];
  }
}



