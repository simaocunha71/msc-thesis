  let arr = test.split(' ')
  let count = {}
  let max = 0
  let res = []

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] in count) {
      count[arr[i]] += 1
    } else {
      count[arr[i]] = 1
    }
    if (count[arr[i]] > max) {
      max = count[arr[i]]
    }
  }

  for (let key in count) {
    if (count[key] === max) {
      res.push({key: key, count: count[key]})
    }
  }
  return res.length === 1 ? {[res[0].key]: res[0].count} : res
}

console.log(histogram('a b c')) //== {'a': 1, 'b': 1, 'c': 1}
console.log(histogram('a b b a')) //== {'a': 2, 'b': 2}
console.log(histogram('a b c a b')) //== {'a': 2, 'b': 2}
console.log(histogram('b b b b a')) //== {'b': 4}
console.log(histogram('')) //== {}

//