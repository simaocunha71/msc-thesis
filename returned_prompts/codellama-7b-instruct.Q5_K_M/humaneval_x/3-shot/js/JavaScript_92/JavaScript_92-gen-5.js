  if (
    !Number.isInteger(x) ||
    !Number.isInteger(y) ||
    !Number.isInteger(z)
  ) {
    return false;
  }

  return x == y + z || y == x + z || z == x + y;
}



