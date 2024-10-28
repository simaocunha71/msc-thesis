  let n = xs.length / 2 - 1;
  let a = xs[n];
  let b = xs[n + 1];
  let c = xs[n + 2];
  let x = -b / (2 * a);
  let y = x * x * c + x * b + a;
  let z = x * x * x * c + x * x * b + x * a + c;
  let t = 1.0 - y / z;
  return x + t;
}