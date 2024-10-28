  const x_arr = x.split('/');
  const n_arr = n.split('/');
  const x_num = parseInt(x_arr[0]);
  const x_denom = parseInt(x_arr[1]);
  const n_num = parseInt(n_arr[0]);
  const n_denom = parseInt(n_arr[1]);
  const prod = x_num * n_denom;
  const div = x_denom * n_num;

  return prod % div == 0;
}



