  let numerator_x = parseInt(x.split('/')[0]);
  let denominator_x = parseInt(x.split('/')[1]);
  let numerator_n = parseInt(n.split('/')[0]);
  let denominator_n = parseInt(n.split('/')[1]);

  let numerator = numerator_x * denominator_n;
  let denominator = denominator_x * numerator_n;

  return (numerator % denominator) === 0;
}