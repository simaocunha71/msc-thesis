  return x.filter(n => {
    return String(n).split('').every(d => +d % 2)
  }).sort((a, b) => a - b)
}



