  let count = 0;
  const getSumOfDigits = (num) => {
    let sum = 0;
    while (num) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    return sum;
  }
  for (let i = 0; i < arr.length; i++) {
    if (getSumOfDigits(arr[i]) > 0) {
      count++;
    }
  }
  return count;
}



