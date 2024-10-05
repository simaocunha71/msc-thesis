  let evenCount = 0;
  let oddCount = 0;
  const numStr = Math.abs(num).toString();

  for  (let i = 0; i < numStr.length; i++)  {
    if  (numStr[i] % 2  === 0)  {
      evenCount++;
    } else  {
      oddCount++;
    }
  }

  return [evenCount, oddCount];
}



