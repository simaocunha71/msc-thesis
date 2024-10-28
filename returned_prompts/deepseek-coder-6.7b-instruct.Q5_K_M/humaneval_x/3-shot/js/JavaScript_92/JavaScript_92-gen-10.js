  return (
    Number.isInteger(x) &&
    Number.isInteger(y) &&
    Number.isInteger(z) &&
    ((x === y + z) || (y === x + z) || (z === x + y))
  );
}



