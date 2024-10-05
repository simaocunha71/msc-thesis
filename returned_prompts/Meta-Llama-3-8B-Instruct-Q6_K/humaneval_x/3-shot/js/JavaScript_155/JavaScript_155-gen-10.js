  let even = 0;
  let odd = 0;

  for (let i = 0; i < num.toString().length; i++) {
    let digit = parseInt(num.toString()[i]);
    if (digit % 2 === 0) {
      even++;
    } else {
      odd++;
    }
  }

  return [even, odd];
}