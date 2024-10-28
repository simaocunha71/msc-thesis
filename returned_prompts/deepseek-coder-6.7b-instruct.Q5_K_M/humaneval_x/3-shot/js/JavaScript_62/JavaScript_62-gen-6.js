  let derivative_coeff = [];
  for  (let i = 1; i < xs.length; i++) {
    derivative_coeff.push(xs[i] * i);
  }
  return derivative_coeff;
}



