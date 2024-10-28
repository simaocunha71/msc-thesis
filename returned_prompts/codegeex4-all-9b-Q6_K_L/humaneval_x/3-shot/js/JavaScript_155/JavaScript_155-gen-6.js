  let str = Math.abs(num).toString();
  let evens = 0;
  let odds = 0;
  for (let i = 0; i < str.length; i++) {
    if (parseInt(str[i]) % 2 == 0) {
      evens += 1;
    } else {
      odds += 1;
    }
  }
  return [evens, odds];
}