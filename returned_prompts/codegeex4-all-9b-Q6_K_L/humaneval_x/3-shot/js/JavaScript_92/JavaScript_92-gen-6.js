  if (x % 1.0 === 0 && y % 1.0 === 0 && z % 1.0 === 0) {
    return (x + y === z) || (x + z === y) || (y + z === x);
  }
  return false;
}