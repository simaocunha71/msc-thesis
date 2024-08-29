  const n1 = parseInt(n.split('/')[1]);
  const x1 = parseInt(x.split('/')[0]);
  const n2 = parseInt(x.split('/')[1]);
  const n3 = parseInt(n.split('/')[0]);

  const lcm = (n1 * n3) / gcd(n1, n3);
  const num1 = (lcm / n1) * x1;
  const num2 = (lcm / n3) * n2;

  if (num1 % n2 === 0) {
    return true;
  } else {
    return false;
  }
}

function gcd(a, b) {
  return a == 0 ? b : gcd(b % a, a);
}



