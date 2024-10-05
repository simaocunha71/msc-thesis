  let evenCount = 0;
  let oddCount = 0;
  let numArray = Math.abs(num).toString().split('');

  for (let i = 0; i < numArray.length; i++) {
    if (numArray[i] % 2 == 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }

  return [evenCount, oddCount];
}



