  let count = 0
  for (let i = 1; i <= n; i++) {
    count += (i.toString()).length === n ? 1 : 0
  }
  return count
}
