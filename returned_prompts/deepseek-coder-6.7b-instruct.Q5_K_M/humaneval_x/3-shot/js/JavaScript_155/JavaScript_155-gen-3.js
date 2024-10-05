  let evenCount = 0;
  let oddCount = 0;
  const digits = Math.abs(num).toString().split('');
  for (let i = 0; i < digits.length; i++) {
    if (digits[i] % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }
  return [evenCount, oddCount];
}



