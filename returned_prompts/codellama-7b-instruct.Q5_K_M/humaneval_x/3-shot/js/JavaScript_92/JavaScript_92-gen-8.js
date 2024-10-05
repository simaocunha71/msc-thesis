  if (x % 1 == 0 && y % 1 == 0 && z % 1 == 0) {
    if (x == y + z || y == x + z || z == x + y) {
      return true;
    }
  }

  return false;
}



