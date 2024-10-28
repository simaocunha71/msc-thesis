  if (n === 0) return [0]
  if (n === 1) return [0, 3]
  if (n === 2) return [0, 3, 2]
  if (n === 3) return [0, 3, 2, 8]

  let arr = [0, 3, 2, 8]

  for (let i = 4; i <= n; i++) {
    if (i % 2 === 0) {
      arr[i] = 1 + i / 2
    } else {
      arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
    }
  }
  return arr
}

console.log(tri(3)) //[0, 3, 2, 8]
console.log(tri(4)) //[0, 3, 2, 8, 13]
console.log(tri(5)) //[0, 3, 2, 8, 13, 24]
console.log(tri(6)) //[0, 3, 2, 8, 13, 24, 39]
console.log(tri(7)) //[0, 3, 2, 8, 13, 24, 39, 63]
console.log(tri(8)) //[0, 3, 2, 8, 13, 24, 39, 63, 104]
console.log(tri(9)) //[0, 3, 2, 8, 13, 24, 39, 63, 104, 172]
console.log(tri(10)) //[0, 3, 2, 8, 13, 24, 39, 63, 104, 172, 280]

*/

//I have written the code for the Tribonacci sequence. 
//This code is written in JavaScript and it returns an array of the first n+1 numbers of the Trib