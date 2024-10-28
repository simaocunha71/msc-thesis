  let str1 = lst[0]
  let str2 = lst[1]
  let count = 0
  
  for (let i = 0; i < str1.length; i++) {
    if (str1[i] === '(') {
      count++
    } else {
      if (count === 0) {
        return 'No'
      }
      count--
    }
  }
  
  for (let i = 0; i < str2.length; i++) {
    if (str2[i] === '(') {
      count++
    } else {
      if (count === 0) {
        return 'No'
      }
      count--
    }
  }
  
  return count === 0 ? 'Yes' : 'No'
}

console.log(matchParens(['()(', ')'])) // 'Yes'
console.log(matchParens([')', ')'])) // 'No'



*/

function matchParens(lst) {
  let str1 = lst[0]
  let str2 = lst[1]
  let count = 0

  for (let i = 0; i < str1.length; i++) {
    if (str1[i] === '(') {
      count++
    } else {
      if (count === 0) {
        return 'No'
      }
      count--
    }
  }

  for (let i = 0; i < str2.length; i++) {
    if (str2[i] === '(') {
      count++
    } else {
      if (count === 0) {
        return 'No'
      }
      count--
    }
  }

  return count === 0 ? 'Yes' : 'No'
}

console.log(matchParens(['()(', ')'])) // 'Yes'
console.log(matchParens([')', ')'])) // 'No'

/*
In the first example:
- str1 = '()('
- str2 = ')'
After concatenating these two strings