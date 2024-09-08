  if (typeof(x) != 'number' || typeof(y) != 'number' || typeof(z) != 'number') {
    return false;
  }
  if (x % 1 != 0 || y % 1 != 0 || z % 1 != 0) {
    return false;
  }
  if (x == (y + z) || y == (x + z) || z == (x + y)) {
    return true;
  } else {
    return false;
  }
}



