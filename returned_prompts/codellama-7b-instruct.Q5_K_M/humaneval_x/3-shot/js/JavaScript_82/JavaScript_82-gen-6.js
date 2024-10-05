  let is_prime = false;

  for (let i = 2; i < string.length; i++) {
    if (string.length % i == 0) {
      is_prime = true;
      break;
    }
  }

  return is_prime;
}



