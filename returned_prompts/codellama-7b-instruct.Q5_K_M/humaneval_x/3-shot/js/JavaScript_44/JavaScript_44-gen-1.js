  if (x < base) {
    return x.toString();
  }

  const digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const quotient = Math.floor(x / base);
  const remainder = x % base;
  return changeBase(quotient, base) + digits[remainder];
}



