const evenOddCount = (num) => {
  let evenCount = 0;
  let oddCount = 0;

  const numStr = num.toString();

  for (let i = 0; i < numStr.length; i++) {
    const digit = numStr[i];
    if (digit % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }

  return [evenCount, oddCount];
};
