  let num1 = parseInt(x.split('/')[0]);
  let denom1 = parseInt(x.split('/')[1]);
  let num2 = parseInt(n.split('/')[0]);
  let denom2 = parseInt(n.split('/')[1]);

  let new_num = num1 * denom2;
  let new_denom = denom1 * num2;

  return new_num === new_denom;
}