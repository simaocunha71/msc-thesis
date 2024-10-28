  if (JSON.stringify(q).split('').sort().join('') !== JSON.stringify(q).split('').reverse().join('')) {
    return false;
  }
  return q.reduce((a, b) => a + b, 0) <= w;
}