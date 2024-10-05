  const asc = l.every((v, i, a) => v >= a[i+1])
  const desc = l.every((v, i, a) => v <= a[i+1])
  return asc || desc
}
