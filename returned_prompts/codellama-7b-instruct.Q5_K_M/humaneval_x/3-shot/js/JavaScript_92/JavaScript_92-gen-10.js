  if (
    Math.floor(x) === x &&
    Math.floor(y) === y &&
    Math.floor(z) === z &&
    (x === y + z || y === x + z || z === x + y)
  ) {
    return true;
  } else {
    return false;
  }
}



