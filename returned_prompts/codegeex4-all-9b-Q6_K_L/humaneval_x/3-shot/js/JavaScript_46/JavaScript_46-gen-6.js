  let arr = [0, 0, 2, 0];

  if (n < 4) {
    return arr[n];
  }

  for (let i = 4; i <= n; i++) {
    arr.push(arr[i - 1] + arr[i - 2] + arr[i - 3] + arr[i - 4]);
  }

  return arr[n];
}