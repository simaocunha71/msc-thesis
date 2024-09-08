  const n = xs.length;
  const a = xs[n - 1];
  const b = xs[n - 2];
  const c = xs[n - 3];
  const d = xs[n - 4];
  const e = Math.pow(b, 2) - 4 * a * c;
  if (e < 0) {
    return null;
  } else if (e === 0) {
    return -b / (2 * a);
  } else {
    const sol1 = (-b + Math.sqrt(e)) / (2 * a);
    const sol2 = (-b - Math.sqrt(e)) / (2 * a);
    return Math.min(sol1, sol2);
  }
}

/*
  >>> round(findRoots([1, 2, 3]), 2)
  [1.0, 2.0]
  >>> round(findRoots([1, 2, -1]), 2)
  [0.5, 1.5]
  >>> round(findRoots([-6, 11, -6, 1]), 2)
  [0.5, 1.0]
  >>> round(findRoots([1, 2, 0]), 2)
  [0.0, 0.0]
  >>> round(findRoots([1, 2, -1]), 2)
  [0.5, 1.5]
  >>> round(findRoots([1, 2, -1]), 2)
  [0.5, 1.5]
  >>> round(findRoots([1, 2, -1]), 2)
  [0.5, 1.5]
  */
const findRoots = (xs) => {
  const zero = findZero(xs);
  if (zero === null) {
    return [];
  } else {
    return [zero];
  }
}

/*
  >>> round(solve([1, 2], [-3, 3]), 2)
  [0.0, 1.0]
  >>> round