const roundedAvg = (n, m) => {
  if (n > m) return -1
  const avg = (n + m) / 2
  return avg.toFixed(0).toString(2)
}

B:
const roundedAvg = (n, m) => {
  if (n > m) return -1
  return Math.round((n + m) / 2).toString(2)
}

C:
const roundedAvg = (n, m) => {
  if (n > m) return -1
  const avg = (n + m) / 2
  return Math.round(avg).toString(2)
}