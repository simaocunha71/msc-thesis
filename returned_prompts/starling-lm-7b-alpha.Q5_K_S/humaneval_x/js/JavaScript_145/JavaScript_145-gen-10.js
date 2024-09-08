  const points = (n) => {
    let total = 0;
    while (n) {
      total += n % 10;
      n = Math.floor(n / 10);
    }
    return total;
  };

  const indexes = (n) => {
    let total = 0;
    while (n) {
      total += n % 10;
      n = Math.floor(n / 10);
    }
    return total;
  };

  return [...nums].sort((a, b) => {
    const ap = points(a);
    const bp = points(b);
    return ap === bp ? indexes(a) - indexes(b) : ap - bp;
  });
};



