  if (typeof(x) == 'number' && typeof(y) == 'number' && typeof(z) == 'number' && Math.floor(x) == x && Math.floor(y) == y && Math.floor(z) == z) {
    if (x + y == z || x + z == y || y + z == x) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}



