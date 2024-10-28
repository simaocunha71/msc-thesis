  var result = [];
  if (a > b) {
    let temp = a;
    a = b;
    b = temp;
  }
  for (let i = a; i <= b; i++) {
    let num = i;
    while (num > 0) {
      let digit = num % 10;
      if (digit % 2 == 0) {
        result.push(digit);
      }
      num = Math.floor(num / 10);
    }
  }
  return result;
}



