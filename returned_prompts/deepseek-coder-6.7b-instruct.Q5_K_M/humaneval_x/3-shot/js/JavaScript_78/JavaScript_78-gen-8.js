  const hexPrimes = new Set(["2", "3", "5", "7", "B", "D"]);
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    if (hexPrimes.has(num[i])) {
      count++;
    }
  }
  return count;
}



