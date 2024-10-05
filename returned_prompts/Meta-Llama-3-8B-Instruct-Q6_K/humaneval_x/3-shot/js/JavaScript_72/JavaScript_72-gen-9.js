  if (q.join('') !== q.join('').split('').reverse().join('')) {
    return false;
  }
  return q.reduce((a, b) => a + b, 0) <= w;
}