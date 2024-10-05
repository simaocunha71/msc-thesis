
// Solution 1 - Regular Expression

  const words = sentence.match(/[a-z]+/g)
  const primeWords = words.filter(word => word.length === 2 || word.length === 3 || word.length === 5 || word.length === 7)
  return primeWords.join(' ')

B:

// Solution 2 - Split and Filter

  const words = sentence.split(' ')
  const primeWords = words.filter(word => word.length === 2 || word.length === 3 || word.length === 5 || word.length === 7)
  return primeWords.join(' ')

C:

// Solution 3 - Split, Filter, Map, Reduce

  const words = sentence.split(' ')
  const primeWords = words.filter(word => word.length === 2 || word.length === 3 || word.length === 5 || word.length === 7).map(word => word.length).reduce((acc, length) => {
    acc[length] ? acc[length]++ : acc[length] = 1
    return acc
  }, {})
  return Object.keys(primeWords).join(' ')
