  let count = 0;
  for (let i = 0; i < num.length; i++) {
    let hex = num[i];
    if (hex === 'B' || hex === 'D' || hex === '5' || hex === '7') {
      count++;
    }
  }
  return count;
}