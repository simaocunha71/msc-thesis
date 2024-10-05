  let even_count = 0;
  let odd_count = 0;

  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    let reverse_str = str.split('').reverse().join('');

    if (str == reverse_str) {
      if (i % 2 == 0) {
        even_count += 1;
      } else {
        odd_count += 1;
      }
    }
  }

  return [even_count, odd_count];
}