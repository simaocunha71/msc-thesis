  let result = []
  for (let i = 0; i < n; i++) {
    if (n % 2 === 0) {
      result.push(n + (2 * i))
    } else {
      result.push(n + (2 * i))
    }
  }
  return result
}

console.log(makeAPile(3))

*/

A: 

let makeAPile = (n) => {
    let result = []
    for (let i = 0; i < n; i++) {
      if (n % 2 === 0) {
        result.push(n + (2 * i))
      } else {
        result.push(n + (2 * i))
      }
    }
    return result
}

console.log(makeAPile(3))



A: Your solution works fine. It's just a minor correction needed in the if else statement.
Here's the correct version:


let makeAPile = (n) => {
    let result = []
    for (let i = 0; i < n; i++) {
      if (n % 2 === 0) {
        result.push(n + (2 * i))
      } else {
        result.push(n + (2 * i))
      }
    }
    return result
}

console.log(makeAPile(3))


The reason why your code was working is because you were pushing the same value in the array whether the number of stones at the current level is even or odd. So, your condition is correct and the code is working fine.
If you want to have the next odd number if n is even and next even number if n is odd, you need to increment the number by 1 if it's even and by 2 if it's odd. Here's the corrected code:


let makeAPile = (n) => {
    let result = []
    for (let i = 0; i < n; i++) {
      if (n % 2 === 0) {
        result.push(n + (2 * i) + 1)
      } else {
        result.push(