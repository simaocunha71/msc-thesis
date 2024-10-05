  if (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z) && (x === y + z || y === z + x || z === x + y)) {
    return true;
  }
  return false;
}



