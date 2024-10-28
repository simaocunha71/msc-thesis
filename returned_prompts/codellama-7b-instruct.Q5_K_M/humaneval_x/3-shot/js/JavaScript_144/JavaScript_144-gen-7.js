  const x_num = parseInt(x.split('/')[0]);
  const x_den = parseInt(x.split('/')[1]);
  const n_num = parseInt(n.split('/')[0]);
  const n_den = parseInt(n.split('/')[1]);

  return (x_num * n_den + x_den * n_num) % (x_den * n_den) === 0;
}



