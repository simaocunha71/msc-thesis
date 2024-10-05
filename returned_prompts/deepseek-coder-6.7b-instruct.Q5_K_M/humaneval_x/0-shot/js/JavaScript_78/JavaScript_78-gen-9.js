  const hexPrimes  [[2, 3, 5, 7, 11, 13], [B, D]];
  let count = 0;

B:
  for (let i = 0; i < num.length; i++) {
    if (hexPrimes[0].includes(parseInt(num[i], 16))) {
      count++;
    }
  }

C:
  for (let i = 0; i < num.length; i++) {
    if (hexPrimes[1].includes(num[i])) {
      count++;
    }
  }

D:
  return count;

E:
};
