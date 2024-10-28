  let odd_num = lst1.filter(num => num % 2 !== 0)
  if(odd_num.length === 0) {
    return "YES"
  }

  let even_num = lst2.filter(num => num % 2 === 0)

  if(odd_num.length > even_num.length) {
    return "NO"
  } else {
    return "YES"
  }

  // odd_num.length <= even_num.length
  // return "YES"
  // odd_num.length > even_num.length
  // return "NO"

}

exchange([1, 2, 3, 4], [1, 2, 3, 4]) // "YES"
exchange([1, 2, 3, 4], [1, 5, 3, 4]) // "NO"
exchange([1, 2, 3, 4], [1, 2, 3, 4, 5]) // "YES"
exchange([1, 2, 3, 4], [1, 2, 3, 4, 6]) // "YES"
exchange([1, 2, 3, 4], [1, 2, 3, 4, 6, 7]) // "NO"

*/





















































































































































































