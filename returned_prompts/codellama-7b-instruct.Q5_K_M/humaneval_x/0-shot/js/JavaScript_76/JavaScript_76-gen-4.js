const isSimplePower = (x, n) => {
  let xn = n ** Math.log2(n);
  return x === xn;
};

/*
  isSimplePower(1, 4)
  =>
  x === 1**Math.log2(4)
  =>
  x === 2
  =>
  true
*/
