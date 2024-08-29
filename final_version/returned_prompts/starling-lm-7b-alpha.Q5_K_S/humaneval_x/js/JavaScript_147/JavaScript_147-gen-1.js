  const a = new Array(n + 1).fill(0).map((_, i) => i * i - i + 1);

  let res = 0;
  for (let i = 1; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      let k = 3 - (a[i] + a[j]) % 3;
      if (k <= 0) continue;
      if (k + a[j] > a[n]) continue;
      res++;
    }
  }
  return res;
}



