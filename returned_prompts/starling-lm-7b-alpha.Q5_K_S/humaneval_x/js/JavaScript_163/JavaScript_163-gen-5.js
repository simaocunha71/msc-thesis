  const digitsA = String(a).split("").map(Number);
  const digitsB = String(b).split("").map(Number);

  const result = [];

  for (const da of digitsA) {
    if (da % 2 == 0) {
      result.push(da);
    }
  }

  for (const db of digitsB) {
    if (db % 2 == 0) {
      result.push(db);
    }
  }

  return result.sort((a, b) => a - b);
}



