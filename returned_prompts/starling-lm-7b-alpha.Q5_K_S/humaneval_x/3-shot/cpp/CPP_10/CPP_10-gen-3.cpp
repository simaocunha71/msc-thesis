  let x_numerator = parseInt(x.split('/')[0]);
  let x_denominator = parseInt(x.split('/')[1]);
  let n_numerator = parseInt(n.split('/')[0]);
  let n_denominator = parseInt(n.split('/')[1]);

  let lcm = (x_denominator * n_denominator) / gcd(x_denominator, n_denominator);

  if ((x_numerator * lcm / x_denominator) % 1 == 0 && (n_numerator * lcm / n_denominator) % 1 == 0) {
    return true;
  } else {
    return false;
  }
}

function gcd(a, b) {
  while (b) {
    const r = a % b;
    a = b;
    b = r;
  }
  return a;
}



