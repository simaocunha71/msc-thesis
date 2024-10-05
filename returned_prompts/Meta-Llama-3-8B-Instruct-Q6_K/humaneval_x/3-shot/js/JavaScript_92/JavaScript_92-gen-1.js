  if (typeof x !== 'number' || typeof y !== 'number' || typeof z !== 'number') {
    return false;
  }
  if (Math.floor(x) !== x || Math.floor(y) !== y || Math.floor(z) !== z) {
    return false;
  }
  return x === y + z || x === z + y || y === z + x || y === x + z || z === x + y || z === y + x;
}