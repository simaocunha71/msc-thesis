/*This function takes a list l and returns a list l' such that
  l' is identical to l in the odd indicies, while its values at the even indicies are equal
  to the values of the even indicies of l, but sorted.
  >>> sortEven([1, 2, 3])
  [1, 2, 3]
  >>> sortEven([5, 6, 3, 4])
  [3, 6, 5, 4]
  */
const sortEven = (l) => {
  const l1 = l.slice()
  const l2 = []
  for (let i = 0; i < l.length; i++) {
    if (i % 2 !== 0) {
      l2.push(l1[i])
    }
  }
  l2.sort((a, b) => a - b)
  for (let i = 0; i < l.length; i++) {
    if (i % 2 === 0) {
      l1[i] = l2[i / 2]
    }
  }
  return l1
}

