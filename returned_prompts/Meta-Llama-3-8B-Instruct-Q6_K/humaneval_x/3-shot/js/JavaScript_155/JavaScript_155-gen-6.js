  let even = 0;
  let odd = 0;

  String(num).split('').forEach(digit => {
    if (parseInt(digit) % 2 === 0) {
      even++;
    } else {
      odd++;
    }
  });

  return [even, odd];
}