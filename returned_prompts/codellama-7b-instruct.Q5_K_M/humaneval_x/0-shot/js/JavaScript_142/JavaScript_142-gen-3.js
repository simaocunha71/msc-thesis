
const sumSquares = (lst) => {
  let squared = []
  let cubed = []
  let sum = 0
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) {
      squared.push(lst[i] ** 2)
    }
    if (i % 4 === 0 && i % 3 !== 0) {
      cubed.push(lst[i] ** 3)
    }
  }
  squared.concat(cubed)
  for (let i = 0; i < squared.length; i++) {
    sum += squared[i]
  }
  return sum
}






