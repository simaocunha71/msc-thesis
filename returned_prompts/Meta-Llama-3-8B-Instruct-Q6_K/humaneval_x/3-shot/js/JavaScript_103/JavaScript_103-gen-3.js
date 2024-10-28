  if (n > m) {
    return -1;
  }
  let sum = 0;
  for (let i = n; i <= m; i++) {
    sum += i;
  }
  let avg = Math.round(sum / (m - n + 1));
  return avg.toString(2);
}  // toString(2) is used to convert the number to binary string.