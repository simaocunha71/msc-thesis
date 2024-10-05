  let count = 0;
  for (let i = 0; i < num.length; i++) {
    let hex = num[i];
    if (hex >= '2' && hex <= '7') {
      count++;
    } else if (hex === 'B' || hex === 'D') {
      count++;
    }
  }
  return count;
}