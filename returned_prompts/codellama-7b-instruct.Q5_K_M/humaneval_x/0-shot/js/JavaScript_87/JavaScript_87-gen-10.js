  return [...lst.flat()]
    .map((v, i) => [i, v])
    .filter(([i, v]) => v === x)
    .sort(([i1, v1], [i2, v2]) => i1 - i2 || v2 - v1)
    .map(([i, v]) => i)
};

