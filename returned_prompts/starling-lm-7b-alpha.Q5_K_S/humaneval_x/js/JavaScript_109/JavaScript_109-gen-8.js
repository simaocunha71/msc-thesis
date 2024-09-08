  let n = arr.length;
  let max = 0;
  for (let i = 1; i < n; i++) {
    if (arr[i] < arr[max]) {
      max = i;
    }
  }
  let idx = 0;
  while (arr[idx] != arr[max]) {
    idx = (idx + 1) % n;
  }
  if (idx == 0) {
    return true;
  } else {
    return false;
  }
}



