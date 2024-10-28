  let even_count = 0;
  let odd_count = 0;

  String(num).split('').forEach(digit => {
    if (parseInt(digit) % 2 === 0) even_count++;
    else odd_count++;
  });

  return [even_count, odd_count];
}