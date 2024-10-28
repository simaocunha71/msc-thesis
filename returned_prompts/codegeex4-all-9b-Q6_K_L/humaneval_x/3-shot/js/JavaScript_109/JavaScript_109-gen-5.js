  let n = arr.length;
  let start = 0;
  let end = 0;

  for (let i = 0; i < n; i++) {
    if (arr[i] <= i) {
      start = i;
    } else {
      break;
    }
  }

  for (let i = n - 1; i >= 0; i--) {
    if (arr[i] >= i) {
      end = i;
    } else {
      break;
    }
  }

  return start <= end;
}