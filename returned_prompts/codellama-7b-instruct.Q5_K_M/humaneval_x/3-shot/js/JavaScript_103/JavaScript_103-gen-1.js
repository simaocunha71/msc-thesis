  if (n > m) return -1;
  let sum = 0;
  for (let i = n; i <= m; i++) {
    sum += i;
  }
  let average = sum / (m-n+1);
  let rounded = Math.round(average);
  return rounded.toString(2);
}



