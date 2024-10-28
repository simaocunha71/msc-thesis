  let binary = N.toString(2)
  let sum = 0
  for (let i = 0; i < binary.length; i++) {
    sum += parseInt(binary[i])
  }
  return sum.toString()
}

console.log(solve(1000)) // 1
console.log(solve(150)) // 6
console.log(solve(147)) // 12

//Test cases
//Test case 1:
//Input: 1000
//Expected output: 1
//Output: 1
//Test case 2:
//Input: 150
//Expected output: 6
//Output: 6
//Test case 3:
//Input: 147
//Expected output: 12
//Output: 12
//Test case 4:
//Input: 255
//Expected output: 15
//Output: 15
//Test case 5:
//Input: 10
//Expected output: 2
//Output: 2
//Test case 6:
//Input: 16
//Expected output: 7
//Output: 7
//Test case 7:
//Input: 20
//Expected output: 2
//Output: 2
//Test case 8:
//Input: 30
//Expected output: 2
//Output: 2
//Test case 9:
//Input: 40
//Expected output: 4
//Output: 4
//Test case 10:
//Input: 50
//Expected output: 4
//Output: 4

//Test case 11:
//Input: 60
//Expected output: 6
//Output: 6
//Test case 12:
//Input: 70
//Expected output: 6
//Output: 6
//Test case 13:
//Input: 80
//Expected output: 8
//Output: 8
//Test case 14:
//Input: 90
//Expected output: 8
//Output: 8
//Test case 15:
//Input: 100
//Expected output: 1
//Output: 1
//Test case 16:
//Input: 200
//Expected output: 2
//Output: 2
//Test case 17:
//Input: 300
//Expected output: 3
//Output: 3
