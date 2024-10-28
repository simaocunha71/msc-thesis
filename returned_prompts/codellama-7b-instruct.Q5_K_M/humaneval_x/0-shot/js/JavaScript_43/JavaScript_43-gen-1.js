  const seen = new Set();
  for (const x of l) {
    if (seen.has(-x)) {
      return true;
    }
    seen.add(x);
  }
  return false;
B:
  return l.some((x, i, a) => a.some((y, j) => j !== i && x + y === 0));
C:
  return l.reduce((acc, x, i, a) => {
    if (i === a.length - 1) return acc;
    for (let j = i + 1; j < a.length; j++) {
      if (a[j] + x === 0) return true;
    }
    return acc;
  }, false);
}



// 1.
// 2.
// 3.




// 1.
const pairsSumToZero = (l) => {
  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      if (l[i] + l[j] === 0) return true;
    }
  }
  return false;
}

// 2.
const pairsSumToZero = (l) => {
  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      if (l[i] + l[j] === 0) return true;
    }
  }
  return false;
}

// 3.
const pairsSumToZero = (l) => {
  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      if (l[i] + l[j] === 0) return true;
    }
  }
  return false;
}
