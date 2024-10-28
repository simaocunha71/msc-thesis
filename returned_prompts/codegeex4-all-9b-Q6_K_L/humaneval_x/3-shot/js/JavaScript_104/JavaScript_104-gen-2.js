  var result = [];
  for (let i = 0; i < x.length; i++) {
    let num = x[i];
    let hasEven = false;
    while (num > 0) {
      let digit = num % 10;
      if (digit % 2 == 0) {
        hasEven = true;
        break;
      }
      num = Math.floor(num / 10);
    }
    if (!hasEven) {
      result.push(x[i]);
    }
  }
  return result.sort((a, b) => a - b);
}



