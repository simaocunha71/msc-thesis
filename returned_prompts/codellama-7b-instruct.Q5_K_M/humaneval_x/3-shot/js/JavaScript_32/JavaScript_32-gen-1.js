  const n = xs.length - 1;
  const m = n / 2;
  const a = xs[n];

  if (a == 0) {
    throw new Error("Polynomial must have nonzero coefficient at the highest degree.");
  }

  const b = xs[m];

  return (-b) / a;
}



