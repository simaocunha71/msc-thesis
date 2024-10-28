  if (x < base) {
    return x.toString();
  }
  return changeBase(Math.floor(x / base), base) + (x % base).toString();
}