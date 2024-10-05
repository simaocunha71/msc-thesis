  let sum = 0;
  for (let i = 0; i < k; i++) {
    let num = arr[i];
    if (Math.floor(Math.log10(Math.abs(num))) <= 2) {
      sum += num;
    } else {
      break;
    }
  }
  return sum;
}