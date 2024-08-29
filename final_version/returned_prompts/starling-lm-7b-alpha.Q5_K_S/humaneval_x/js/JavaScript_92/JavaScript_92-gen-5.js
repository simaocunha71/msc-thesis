  if (typeof(x) === "number" && typeof(y) === "number" && typeof(z) === "number") {
    if (x % 1 === 0 && y % 1 === 0 && z % 1 === 0) {
      return (x === (y + z)) || (y === (x + z)) || (z === (x + y));
    }
  }
  return false;
}



