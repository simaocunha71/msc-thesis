  const numStr = Math.abs(num).toString();
  const evenCount = Array.from(numStr).filter(n => n % 2 === 0).length;
  const oddCount = numStr.length - evenCount;
  return [evenCount, oddCount];
}



