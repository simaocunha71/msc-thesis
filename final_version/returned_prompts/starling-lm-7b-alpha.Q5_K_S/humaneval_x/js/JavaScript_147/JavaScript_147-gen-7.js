  let a = [];
  for (let i = 1; i <= n; i++) {
    a.push(i * i - i + 1);
  }
  let count = 0;
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < a.length; j++) {
      for (let k = 0; k < a.length; k++) {
        if (i < j && j < k && (a[i] + a[j] + a[k]) % 3 === 0) {
          count += 1;
        }
      }
    }
  }
  return count;
}



