  let num_str = "" + num;
  let even_count = 0;
  let odd_count = 0;

  for (let i = 0; i < num_str.length; i++) {
    if (num_str[i] % 2 == 0) {
      even_count += 1;
    } else {
      odd_count += 1;
    }
  }

  return [even_count, odd_count];
}


