/*Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
  

  Examples
  solution([5, 8, 7, 1]) ==> 12
  solution([3, 3, 3, 3, 3]) ==> 9
  solution([30, 13, 24, 321]) ==>0
  */
const solution = (lst) => {
  let sum = 0
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 !== 0) {
      sum += lst[i]
    }
  }
  return sum
}

/*Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
  

  Examples
  solution([5, 8, 7, 1]) ==> 12
  solution([3, 3, 3, 3, 3]) ==> 9
  solution([30, 13, 24, 321]) ==>0
  */
const solution = (lst) => {
  let sum = 0
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 === 0) {
      sum += lst[i]
    }
  }
  return sum
}

/*Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
  

  Examples
  solution([5, 8, 7, 1]) ==> 12
  solution([3, 3, 3, 3, 3]) ==> 9
  solution([30, 13, 24, 321]) ==>0
  */
const solution = (lst) => {
  let sum = 0
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 === 