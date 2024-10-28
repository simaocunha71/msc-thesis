  if (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) {
    if (x == y + z || y == x + z || z == x + y) {
      return true;
    }
  }
  return false;
}



