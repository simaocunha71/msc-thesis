  return x.filter((e) => {
    for (const digit of e.toString()) {
      if (digit % 2 == 0) {
        return false;
      }
    }
    return true;
  }).sort((a, b) => a - b);
}



