  let [num_x, den_x] = x.split('/');
  let [num_n, den_n] = n.split('/');

  let num_product = parseInt(num_x) * parseInt(num_n);
  let den_product = parseInt(den_x) * parseInt(den_n);

  if (num_product % den_product == 0) {
    return true;
  } else {
    return false;
  }
}



