  const hexPrimeCounts = {
    '2': 1, '3': 1, '5': 1, '7': 1,
    'A': 1, 'B': 1, 'D': 1, 'E': 1
  };
  let count = 0;
  for  (const c of num) {
    if  (hexPrimeCounts[c] === 1) {
      count += 1;
    }
  }
  return count;
}



