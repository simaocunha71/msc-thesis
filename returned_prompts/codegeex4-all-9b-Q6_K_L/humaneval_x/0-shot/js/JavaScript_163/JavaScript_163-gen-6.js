const generateIntegers = (a, b) => {
  let nums = []
  for (let i = a; i <= b; i++) {
    if (i % 2 === 0) {
      nums.push(i)
    }
  }
  return nums
}

console.log(generateIntegers(2, 8)) // [2, 4, 6, 8]
console.log(generateIntegers(8, 2)) // [2, 4, 6, 8]
console.log(generateIntegers(10, 14)) // []
console.log(generateIntegers(25, 30)) // [26, 28, 30]
console.log(generateIntegers(100, 200)) // [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]