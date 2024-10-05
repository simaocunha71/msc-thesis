  let evenCount = 0;
  let oddCount = 0;
  let numStr = num.toString();
  for (let i = 0; i < numStr.length; i++) {
    let digit = parseInt(numStr[i]);
    if (digit % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }
  return [evenCount, oddCount];
}
