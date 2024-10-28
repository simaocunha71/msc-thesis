  let even = 0;
  let odd = 0;

  num = Math.abs(num).toString();

  for (let i = 0; i < num.length; i++) {
    if (parseInt(num[i]) % 2 === 0) {
      even++;
    } else {
      odd++;
    }
  }

  return [even, odd];
}