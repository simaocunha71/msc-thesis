  let arr = [];
  for (let i = 1; i <= n; i++) {
    arr.push(i * i - i + 1);
  }

  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      for (let k = j + 1; k < arr.length; k++) {
        if ((arr[i] + arr[j] + arr[k]) % 3 == 0) {
          count += 1;
        }
      }
    }
  }
  return count;
}


