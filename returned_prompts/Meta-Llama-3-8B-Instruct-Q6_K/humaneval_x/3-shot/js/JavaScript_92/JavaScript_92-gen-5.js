  return (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) &&
         (x === y + z || x === z + y || y === x + z || y === z + x || z === x + y || z === y + x);
}