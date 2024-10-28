  let count = 0;
  let array = [];
  for (let i = 1; i <= n; i++) {
    array.push(i * i - i + 1);
  }
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        if ((array[i] + array[j] + array[k]) % 3 === 0) {
          count++;
        }
      }
    }
  }
  return count;
}