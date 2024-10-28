function filterIntegers(values) {
  return values.filter(v => typeof v === 'number' && Number.isInteger(v));
}














/*
  >>> filterList([1, 2, 3, 4], 2)
  [2]
  >>> filterList([1, 2, 3, 4], 5)
  []
  >>> filterList([10, 20, 30, 40], 0)
  [0]
  */


const filterList = (arr, num) => {
  return arr.filter(v => v === num);
}

































/*
  >>> listSum([1, 2, 3, 4])
  10
  >>> listSum([10, 20, 30, 40])
  100
  >>> listSum([])
  0
  */

const listSum = (arr) => {
  return arr.reduce((acc, cur) => acc + cur, 0);
}






































/*
  >>> listDiff([1, 2, 3, 4], [3, 4, 5, 6])
  [1, 2]
  >>> listDiff([1, 2, 3, 4], [])
  [1, 2, 3, 4]
  >>> listDiff([], [3, 4, 5, 6])
  []
  */

const listDiff = (arr1, arr2) => {
  return arr1.filter(v => !arr2.includes(v));
}









































/*
  >>> listProduct([2, 2, 2