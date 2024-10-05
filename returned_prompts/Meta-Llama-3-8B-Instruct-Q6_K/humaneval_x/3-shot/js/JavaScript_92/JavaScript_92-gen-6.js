  if (!Number.isInteger(x) || !Number.isInteger(y) || !Number.isInteger(z)) {
    return false;
  }
  return (x === y + z) || (x === z + y) || (y === x + z) || (y === z + x) || (z === x + y) || (z === y + x);
}