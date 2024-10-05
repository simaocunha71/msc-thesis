
  let largest = lst.reduce((acc, curr) => {
    if (curr > acc) {
      return curr
    } else {
      return acc
    }
  }, 0)
  return largest.toString().split('').reduce((acc, curr) => {
    return acc + +curr
  }, 0)
}


