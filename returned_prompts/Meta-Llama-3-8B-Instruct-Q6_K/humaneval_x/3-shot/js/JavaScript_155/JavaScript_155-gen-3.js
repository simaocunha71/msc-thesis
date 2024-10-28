  let even_count = 0;
  let odd_count = 0;

  for (let digit of num.toString().split('')) {
    if (+digit % 2 === 0) {
      even_count++;
    } else {
      odd_count++;
    }
  }

  return [even_count, odd_count];
}