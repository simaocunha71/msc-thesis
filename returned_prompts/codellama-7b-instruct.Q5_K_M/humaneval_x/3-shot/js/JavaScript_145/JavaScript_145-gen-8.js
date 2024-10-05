  nums.sort((a, b) => {
    const sumA = getSumOfDigits(a);
    const sumB = getSumOfDigits(b);
    if (sumA != sumB) {
      return sumA - sumB;
    } else {
      return a - b;
    }
  });

  return nums;
}

const getSumOfDigits = (num) => {
  let sum = 0;
  while (num > 0) {
    sum += num % 10;
    num = num / 10 | 0;
  }

  return sum;
}



