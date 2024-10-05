  let count = 0;
  let arr = new Array(n);
  for (let i = 0; i < n; i++) {
    arr[i] = i * i - i + 1;
  }
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        if ((arr[i] + arr[j] + arr[k]) % 3 === 0) {
          count++;
        }
      }
    }
  }
  return count;
}