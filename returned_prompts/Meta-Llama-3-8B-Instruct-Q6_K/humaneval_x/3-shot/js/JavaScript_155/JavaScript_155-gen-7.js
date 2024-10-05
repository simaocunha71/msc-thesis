  let even_count = 0;
  let odd_count = 0;
  let num_str = Math.abs(num).toString();
  
  for (let i = 0; i < num_str.length; i++) {
    let digit = parseInt(num_str[i]);
    if (digit % 2 === 0) {
      even_count++;
    } else {
      odd_count++;
    }
  }
  return [even_count, odd_count];
}