  let i = a.indexOf(b)
  if (i !== -1) return true
  for (let i = 0; i < b.length; i++) {
    if (a.includes(b.slice(i) + b.slice(0, i))) return true
  }
  return false
}

