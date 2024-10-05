  /*
    O(N) time complexity
    O(N) space complexity
  */
  if (lst.length === 0) {
    return null
  }
  let min = null
  for (let i = 0; i < lst.length; i++) {
    if (min === null) {
      min = lst[i]
    }
    if (lst[i] < min) {
      min = lst[i]
    }
  }
  if (min === null) {
    return null
  }
  let count = 0
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] === min) {
      if (i + 1 < lst.length && lst[i + 1] > min) {
        return lst[i + 1]
      } else if (i + 2 < lst.length && lst[i + 2] > min) {
        return lst[i + 2]
      }
    }
  }
  return null
}
