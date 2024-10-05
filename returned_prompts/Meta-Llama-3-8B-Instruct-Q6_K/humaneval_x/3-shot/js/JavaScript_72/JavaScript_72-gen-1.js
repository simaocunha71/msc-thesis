  const qStr = q.join('');
  if (qStr !== qStr.split('').reverse().join('')) {
    return false;
  }
  return q.reduce((acc, curr) => acc + curr) <= w;
}