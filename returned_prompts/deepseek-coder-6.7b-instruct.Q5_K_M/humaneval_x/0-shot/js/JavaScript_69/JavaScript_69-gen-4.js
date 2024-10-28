  const counts = lst.reduce((acc, v) => {
    acc[v] = (acc[v] || 0) + 1
    return acc
  }, {})

  let max = -1
  for (let key in counts) {
    if (key >= counts[key] && key > max) {
      max = key
    }
  }
  return max === -1 ? -1 : parseInt(max)
}
console.log(search([4, 1, 2, 2, 3, 1]))
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
console.log(search([5, 5, 4, 4, 4]))

// Tests:
console.log(search([4, 1, 2, 2, 3, 1]) === 2)
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4]) === 3)
console.log(search([5, 5, 4, 4, 4]) === -1)

// Returns the integer that appears most frequently in the list, but only if that frequency is greater than or equal to the integer value itself. If no such integer exists, return -1.


*/
