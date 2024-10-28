  let x_num = parseInt(x.split('/')[0]);
  let x_den = parseInt(x.split('/')[1]);

  let n_num = parseInt(n.split('/')[0]);
  let n_den = parseInt(n.split('/')[1]);

  return x_num * n_den === x_den * n_num;
}



