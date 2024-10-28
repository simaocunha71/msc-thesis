const anyInt = (x, y, z) => {
  if (typeof x !== 'number' || typeof y !== 'number' || typeof z !== 'number') {
    return false
  }
  if (x % 1 !== 0 || y % 1 !== 0 || z % 1 !== 0) {
    return false
  }
  return x === y + z || y === z + x || z === x + y
}


