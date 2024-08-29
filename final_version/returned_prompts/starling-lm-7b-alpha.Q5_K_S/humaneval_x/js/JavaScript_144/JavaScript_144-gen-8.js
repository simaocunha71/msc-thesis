  let numerator_x = parseInt(x.split("/")[0]);
  let denominator_x = parseInt(x.split("/")[1]);
  let numerator_n = parseInt(n.split("/")[0]);
  let denominator_n = parseInt(n.split("/")[1]);

  let lcm = (denominator_x * denominator_n) / gcd(denominator_x, denominator_n);

  let numerator = numerator_x * (lcm / denominator_x) +
                  numerator_n * (lcm / denominator_n);

  if (numerator % 1 === 0) {
    return true;
  } else {
    return false;
  }
}

const gcd = (a, b) => {
  while (b) {
    let t = a % b;
    a = b;
    b = t;
  }
  return a;
}



