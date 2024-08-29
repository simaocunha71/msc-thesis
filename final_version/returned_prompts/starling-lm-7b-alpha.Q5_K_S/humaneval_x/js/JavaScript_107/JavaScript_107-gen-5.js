  let even_pal = 0;
  let odd_pal = 0;
  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    if (str == str.split('').reverse().join('')) {
      if (i % 2 == 0) {
        even_pal += 1;
      } else {
        odd_pal += 1;
      }
    }
  }
  return [even_pal, odd_pal];
}



