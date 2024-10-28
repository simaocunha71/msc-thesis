const changeBase = (x, base) => {
  const res = [];
  while (x > 0) {
    res.push(x % base);
    x = Math.floor(x / base);
  }
  return res.reverse().join('');
};

