  let i = 0;
  let current = 1;
  while (current < x) {
    current *= n;
    i += 1;
  }
  return i > 0 && current == x;
}



