  const [x_n, x_d] = x.split('/');
  const [n_n, n_d] = n.split('/');

  const x_value = x_n / x_d;
  const n_value = n_n / n_d;

  return x_value % n_value == 0;
}



