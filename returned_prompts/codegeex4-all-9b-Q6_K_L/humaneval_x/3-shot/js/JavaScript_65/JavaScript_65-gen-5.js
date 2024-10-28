  let s = x.toString();
  shift %= s.length;
  return s.slice(-shift) + s.slice(0, -shift);
}