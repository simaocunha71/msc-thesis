  let numerator = Number(x.split('/')[0]);
  let denominator = Number(x.split('/')[1]);
  let numerator2 = Number(n.split('/')[0]);
  let denominator2 = Number(n.split('/')[1]);
  return ((numerator * denominator2) % (denominator * numerator2) == 0);
}