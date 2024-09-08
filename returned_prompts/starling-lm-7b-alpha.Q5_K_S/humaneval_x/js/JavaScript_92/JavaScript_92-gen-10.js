  if (typeof(x) === 'number' && typeof(y) === 'number' && typeof(z) === 'number') {
    if (x == Math.floor(x) && y == Math.floor(y) && z == Math.floor(z)) {
      if (x + y == z || x + z == y || y + z == x) {
        return true;
      }
    }
  }
  return false;
}



