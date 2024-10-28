  const arr = test.split(' ')
  let count = {}
  let max = 0
  let result = {}

  for (let letter of arr) {
    if (count[letter]) {
      count[letter]++
    } else {
      count[letter] = 1
    }

    if (count[letter] > max) {
      max = count[letter]
    }
  }

  for (let key in count) {
    if (count[key] === max) {
      result[key] = max
    }
  }

  return result
}

console.log(histogram('a b c')) //  {'a': 1, 'b': 1, 'c': 1}
console.log(histogram('a b b a')) //  {'a': 2, 'b': 2}
console.log(histogram('a b c a b')) //  {'a': 2, 'b': 2}
console.log(histogram('b b b b a')) //  {'b': 4}
console.log(histogram('')) //  {}

*/




















































































































































































































































