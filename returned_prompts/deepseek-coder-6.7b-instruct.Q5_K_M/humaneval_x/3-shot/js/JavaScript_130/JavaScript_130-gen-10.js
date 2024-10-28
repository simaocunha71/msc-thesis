  let arr = [0, 3, 2];
  for (let i = 3; i <= n; i++) {
    if (i % 2 === 0) {
      arr[i] = 1 + i / 2;
    } else {
      arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
    }
  }
  return arr.slice(1, n + 1);
}



