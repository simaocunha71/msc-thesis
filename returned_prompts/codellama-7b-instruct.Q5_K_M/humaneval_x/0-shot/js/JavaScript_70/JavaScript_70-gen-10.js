const strangeSortList = (lst) => {
  return lst.sort((a, b) => a - b).reverse()
}

B:
const strangeSortList = (lst) => {
  return lst.sort((a, b) => b - a)
}

C:
const strangeSortList = (lst) => {
  return lst.sort((a, b) => a % 2 === 0 ? -1 : 1)
}

D:
const strangeSortList = (lst) => {
  return lst.sort((a, b) => b % 2 === 0 ? 1 : -1)
}
