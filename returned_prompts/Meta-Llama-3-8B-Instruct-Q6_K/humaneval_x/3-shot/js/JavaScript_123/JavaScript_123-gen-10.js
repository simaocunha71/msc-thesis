  let sequence = [];
  let num = n;
  while (num != 1) {
    if (num % 2 != 0) {
      sequence.push(num);
    }
    if (num % 2 == 0) {
      num = Math.floor(num / 2);
    } else {
      num = num * 3 + 1;
    }
  }
  sequence.push(1);
  return sequence.sort((a, b) => a - b);
}