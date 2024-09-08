  let p = (a + b + c) / 2;
  let sqrt_p = Math.sqrt(p * (p - a) * (p - b) * (p - c));
  return (p * sqrt_p) % 1 === 0;
}



