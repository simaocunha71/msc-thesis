  let result = [];

  for (let i = 0; i < x.length; i++) {
    let current_number = x[i];
    let has_even_digit = false;

    while (current_number > 0) {
      if (current_number % 10 % 2 == 0) {
        has_even_digit = true;
        break;
      }
      current_number = current_number / 10;
    }

    if (!has_even_digit) {
      result.push(x[i]);
    }
  }

  return result.sort((a, b) => a - b);
}



