  let count = 0;
  for (let i = 0; i < num.length; i++) {
    let c = num[i];
    if (c >= '2' && c <= '7') {
      count++;
    } else if (c === 'B' || c === 'D') {
      count++;
    }
  }
  return count;
}