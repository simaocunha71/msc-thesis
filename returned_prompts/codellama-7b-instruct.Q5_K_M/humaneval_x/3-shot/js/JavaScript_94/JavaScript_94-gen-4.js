  if (number == 1 || number == 0) return false;
  if (number == 2 || number == 3) return true;

  for (let i = 2; i < Math.floor(number ** 0.5); i++) {
    if (number % i == 0) return false;
  }

  return true;
}



