  return arr.sort((a, b) => {
    const a_ones = a.toString(2).match(/1/g) || []
    const b_ones = b.toString(2).match(/1/g) || []

    if (a_ones.length !== b_ones.length) {
      return a_ones.length - b_ones.length
    } else {
      return a - b
    }
  })
}



