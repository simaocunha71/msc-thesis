  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    let digits = String(arr[i]).split('').map(x => +x);
    for (let j = 0; j < digits.length; j++) {
      sum += Math.abs(digits[j]);
    }
    if (sum > 0) {
      count += 1;
    }
  }
  return count;
}



