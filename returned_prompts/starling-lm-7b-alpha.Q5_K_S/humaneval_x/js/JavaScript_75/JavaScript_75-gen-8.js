  const prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
  let number = a;
  let result = true;

  for (let i = 0; i < prime_numbers.length; i++) {
    if (prime_numbers[i] > number) {
      break;
    }

    if (number % prime_numbers[i] == 0) {
      number = number / prime_numbers[i];
    } else {
      result = false;
      break;
    }
  }

  if (result && number == 1) {
    result = true;
  } else {
    result = false;
  }

  return result;
}



