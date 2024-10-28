  const numerator_x = parseInt(x.split('/')[0]);
  const denominator_x = parseInt(x.split('/')[1]);
  const numerator_n = parseInt(n.split('/')[0]);
  const denominator_n = parseInt(n.split('/')[1]);

  return (numerator_x * denominator_n) % (numerator_n * denominator_x) == 0;
}