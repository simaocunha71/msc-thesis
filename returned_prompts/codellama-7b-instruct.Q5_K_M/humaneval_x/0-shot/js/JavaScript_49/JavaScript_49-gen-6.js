  /*
  let p = 101;
  let n = 1101;
  let p_ = 1;
  let n_ = 2;
  */

  let p_ = n % p;
  let n_ = n / p;

  if (n_ > 1) {
    return modp(n_, p_) + p_;
  }
  else {
    return n_;
  }
};
