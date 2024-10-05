  let length = string.length;
  let is_prime = false;

  for (let i = 2; i < length; i++) {
    if (length % i == 0) {
      break;
    } else {
      is_prime = true;
    }
  }

  return is_prime;
}



