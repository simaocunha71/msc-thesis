  const isSubStr = (str1, str2) => str1.includes(str2)

  if (a.length < b.length) return false
  if (a === b) return true

  for (let i = 0; i < b.length; i++) {
    const rot = b.slice(i) + b.slice(0, i)
    if (isSubStr(a, rot)) return true
  }
  return false
}

