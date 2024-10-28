

  const countFruits = (s, n) => {
    const split = s.split(" ")
    const numApples = +split[0]
    const numOranges = +split[2]
    const totalFruits = n - numApples - numOranges
    return totalFruits
  }

  const numMango = countFruits(s, n)
  return numMango
}







