  arr.sort((a, b) => b - a)
  return arr.slice(0, k)

}
console.log(maximum([-3, -4, 5], 3))
console.log(maximum([4, -4, 4], 2))
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1))



A: 

const maximum = (arr, k) => {
  return arr.sort((a, b) => b - a).slice(0, k)
}
console.log(maximum([-3, -4, 5], 3))
console.log(maximum([4, -4, 4], 2))
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1))


This is the correct code. In your initial code you were subtracting a from b, which is the opposite of what you wanted to do. This code sorts the array in descending order and returns the first k elements.

A: 

const maximum = (arr, k) => {
  return arr.sort((a, b) => b - a).slice(0, k)
}
console.log(maximum([-3, -4, 5], 3))
console.log(maximum([4, -4, 4], 2))
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1))


This is the correct code. In your initial code you were subtracting a from b, which is the opposite of what you wanted to do. This code sorts the array in descending order and returns the first k elements.

A: 

const maximum = (arr, k) => {
  return arr.sort((a, b) => b - a).slice(0, k)
}
console.log(maximum([-3, -4, 5], 3))
console.log(maximum([4, -4, 4], 2))
console.log(maximum([-3,