  let result = [];
  let num = n;
  while (num !== 1) {
    if (num % 2 === 1) {
      result.push(num);
    }
    if (num % 2 === 0) {
      num = Math.floor(num / 2);
    } else {
      num = num * 3 + 1;
    }
  }
  return result.sort((a, b) => a - b);
}