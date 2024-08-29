  let max_prime_value = Math.max(...lst);
  let max_prime_value_str = max_prime_value.toString();
  let sum_of_digits = 0;

  for (let i = 0; i < max_prime_value_str.length; i++) {
    sum_of_digits += parseInt(max_prime_value_str[i]);
  }

  return sum_of_digits;
}



