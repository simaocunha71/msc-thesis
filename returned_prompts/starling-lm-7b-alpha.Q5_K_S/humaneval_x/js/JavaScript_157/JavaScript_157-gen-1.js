  if (a < 0 || b < 0 || c < 0) {
    return false;
  }

  let a_sq = Math.pow(a, 2);
  let b_sq = Math.pow(b, 2);
  let c_sq = Math.pow(c, 2);

  return (a_sq + b_sq == c_sq) || (c_sq + b_sq == a_sq) || (c_sq + a_sq == b_sq);
}



