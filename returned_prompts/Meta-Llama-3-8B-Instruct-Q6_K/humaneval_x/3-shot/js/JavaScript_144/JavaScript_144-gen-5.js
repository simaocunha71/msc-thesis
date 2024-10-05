  let num_x = parseInt(x.split('/')[0]);
  let den_x = parseInt(x.split('/')[1]);
  let num_n = parseInt(n.split('/')[0]);
  let den_n = parseInt(n.split('/')[1]);

  let new_num = num_x * den_n;
  let new_den = den_x * num_n;

  return new_num % new_den === 0;
}
}  // end of the problem set.