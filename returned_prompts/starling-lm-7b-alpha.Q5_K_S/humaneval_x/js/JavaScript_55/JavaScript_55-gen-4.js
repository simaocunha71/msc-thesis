  if (n <= 2) return 1;

  let a = 1;
  let b = 1;
  let c = 0;
  while (n > 3) {
    c = a + b;
    a = b;
    b = c;
    n--;
  }

  return c;
}



