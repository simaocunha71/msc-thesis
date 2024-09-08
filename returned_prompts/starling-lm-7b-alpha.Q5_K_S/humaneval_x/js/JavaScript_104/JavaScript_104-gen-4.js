  const hasEven = (n) => {
    while (n > 0) {
      if (n % 10 % 2 == 0) return true;
      n = Math.floor(n / 10);
    }
    return false;
  };

  const sort = (ns) => {
    for (let i = 0; i < ns.length; i++) {
      for (let j = i + 1; j < ns.length; j++) {
        if (ns[i] > ns[j]) {
          [ns[i], ns[j]] = [ns[j], ns[i]];
        }
      }
    }
  };

  const ns = [];
  for (const n of x) {
    if (!hasEven(n)) ns.push(n);
  }
  sort(ns);

  return ns;
}



