  let [numerator, denominator] = x.split('/');
  let [numerator_n, denominator_n] = n.split('/');

  let result_numerator = numerator * numerator_n;
  let result_denominator = denominator * denominator_n;

  let gcd = (a, b) => {
    if (b == 0) { return a; }
    return gcd(b, a % b);
  }

  result_numerator = result_numerator / gcd(result_numerator, result_denominator);
  result_denominator = result_denominator / gcd(result_numerator, result_denominator);

  return result_numerator % result_denominator === 0;
}



