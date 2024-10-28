  if (typeof x != 'number' || typeof y != 'number' || typeof z != 'number') {
    return false;
  }

  if (Math.floor(x) !== x || Math.floor(y) !== y || Math.floor(z) !== z) {
    return false;
  }

  if (x === y + z || y === x + z || z === x + y) {
    return true;
  } else {
    return false;
  }
}



