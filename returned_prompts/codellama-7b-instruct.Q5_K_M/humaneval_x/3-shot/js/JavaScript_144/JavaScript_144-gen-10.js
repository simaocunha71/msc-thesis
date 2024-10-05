  const x_num = parseInt(x.split('/')[0]);
  const x_denom = parseInt(x.split('/')[1]);
  const n_num = parseInt(n.split('/')[0]);
  const n_denom = parseInt(n.split('/')[1]);

  return (x_num * n_denom) % (x_denom * n_num) == 0;
}



