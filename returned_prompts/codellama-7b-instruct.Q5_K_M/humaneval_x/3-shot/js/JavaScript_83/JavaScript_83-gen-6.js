  if (n < 1) return 0;

  const num_digits = 10 ** n;
  const num_ones = num_digits - 10 ** (n - 1);

  return num_ones * 2;
}



