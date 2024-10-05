  let primeHex = ['2', '3', '5', '7', 'B', 'D'];
  let count = 0;
  for (let i = 0; i < num.length; i++) {
    if (primeHex.indexOf(num[i]) !== -1) {
      count++;
    }
  }
  return count;
}


