  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (arr[i].toString().length <= 2) {
      sum += arr[i];
    }
  }
  return sum;
}



