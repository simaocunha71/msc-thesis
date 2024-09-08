  if (typeof(x) != "number" || typeof(y) != "number" || typeof(z) != "number") {
    return false;
  }
  if (x == Math.floor(x) && y == Math.floor(y) && z == Math.floor(z)) {
    return (x + y == z) || (x + z == y) || (y + z == x);
  } else {
    return false;
  }
}



