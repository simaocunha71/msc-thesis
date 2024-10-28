  const [numerator_x, denominator_x] = x.split('/');
  const [numerator_n, denominator_n] = n.split('/');

  const numerator_result = numerator_x * numerator_n;
  const denominator_result = denominator_x * denominator_n;

  return (numerator_result % denominator_result === 0);
}



