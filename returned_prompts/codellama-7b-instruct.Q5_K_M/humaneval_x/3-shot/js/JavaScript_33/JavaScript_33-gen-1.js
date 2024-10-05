  return l.map((x, i) => i % 3 ? x : [...l].filter((_, j) => j % 3 == i).sort()[0])
}



