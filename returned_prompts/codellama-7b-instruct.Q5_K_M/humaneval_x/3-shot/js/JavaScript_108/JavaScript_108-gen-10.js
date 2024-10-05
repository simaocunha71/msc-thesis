  var count = 0;

  for (const e of arr) {
    var signed_digits = [...String(Math.abs(e))].map(Number);
    var sum = signed_digits.reduce((a, b) => a + b);
    if (sum > 0) count += 1;
  }

  return count;
}



