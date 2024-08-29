  let result = 0;
  for (const num of arr) {
    let sum = Math.abs(num).toString().split('').reduce((sum, digit) => sum + parseInt(digit), 0);
    if (sum > 0) result += 1;
  }
  return result;
}



