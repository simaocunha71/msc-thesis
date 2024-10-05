/*
  Solution:
  The solution to this problem is to iterate through the lists and check if the
  element is even or odd. If the element is odd, then it is possible to exchange
  the element with the element of the other list.
  */
  const lst1IsEven = lst1.every(el => el % 2 === 0)
  const lst2IsEven = lst2.every(el => el % 2 === 0)
  if (lst1IsEven && lst2IsEven) {
    return "YES"
  } else if (lst1IsEven || lst2IsEven) {
    return "NO"
  } else {
    for (let i = 0; i < lst1.length; i++) {
      if (lst1[i] % 2 === 0) {
        for (let j = 0; j < lst2.length; j++) {
          if (lst2[j] % 2 !== 0) {
            [lst1[i], lst2[j]] = [lst2[j], lst1[i]]
            break
          }
        }
      }
    }
    return lst1.every(el => el % 2 === 0) ? "YES" : "NO"
  }
}
