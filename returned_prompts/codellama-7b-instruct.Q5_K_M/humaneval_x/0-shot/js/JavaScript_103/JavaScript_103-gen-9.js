/*
  const roundedAvg = (n, m) => {
  if (n > m) return -1
  const avg = (n + m) / 2
  return (avg | 0).toString(2)
  }
  */
  return (n > m) ? -1 : ((n + m) / 2 | 0).toString(2)
}
