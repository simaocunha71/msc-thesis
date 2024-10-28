  const result = 0

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] % 2 === 0 && i % 2 !== 0) {
      result += lst[i]
    }
  }
  return result
}

