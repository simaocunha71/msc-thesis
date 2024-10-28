  return arr.sort((a, b) => {
    if (countBits(a) == countBits(b)) {
      return a - b;
    }
    return countBits(a) - countBits(b);
  });
}



