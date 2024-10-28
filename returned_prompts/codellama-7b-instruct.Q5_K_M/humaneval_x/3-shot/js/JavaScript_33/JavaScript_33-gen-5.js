  var result = l.filter((_, i) => i % 3 != 0).sort((a, b) => a - b)

  for (let i = 0; i < l.length; i += 3) {
    result.splice(i, 0, l[i])
  }

  return result
}



