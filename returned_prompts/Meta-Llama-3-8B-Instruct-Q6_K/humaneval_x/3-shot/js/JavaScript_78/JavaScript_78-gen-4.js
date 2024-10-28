  let count = 0;
  for (const char of num) {
    if (char === '2' || char === '3' || char === '5' || char === '7' || char === 'B' || char === 'D' || char === 'F') {
      count++;
    }
  }
  return count;
}