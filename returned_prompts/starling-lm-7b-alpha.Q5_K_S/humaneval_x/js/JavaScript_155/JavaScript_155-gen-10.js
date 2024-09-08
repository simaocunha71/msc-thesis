  let evenCount = 0;
  let oddCount = 0;

  let numStr = num.toString();

  for (let i = 0; i < numStr.length; i++) {
    let char = numStr[i];
    if (char % 2 == 0) {
      evenCount += 1;
    } else {
      oddCount += 1;
    }
  }

  return [evenCount, oddCount];
}



