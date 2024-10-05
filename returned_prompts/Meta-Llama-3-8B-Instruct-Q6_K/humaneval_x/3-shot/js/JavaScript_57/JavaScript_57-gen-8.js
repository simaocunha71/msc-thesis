  return l.every((x, i, a) => i === 0 ? true : x >= a[i - 1]) || l.every((x, i, a) => i === 0 ? true : x <= a[i - 1]);
}