  const test = 'a b c a b c a b c'
  var result = {}
  var temp = ''
  for (var i = 0; i < test.length; i++) {
      if (test[i] !== ' ') {
          temp += test[i]
      } else {
          if (result[temp]) {
              result[temp] += 1
          } else {
              result[temp] = 1
          }
          temp = ''
      }
  }
  return result
}