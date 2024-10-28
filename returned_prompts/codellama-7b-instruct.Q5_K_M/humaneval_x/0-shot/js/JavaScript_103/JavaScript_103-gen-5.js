/*You are given two positive integers n and m. If n is greater than m, return -1.
  Otherwise, return the average of the integers from n through m (including n and m). 
  Round the answer to the nearest integer and convert that to binary.
  Example:
  roundedAvg(1, 5) => "0b11"
  roundedAvg(7, 5) => -1
  roundedAvg(10, 20) => "0b1111"
  roundedAvg(20, 33) => "0b11010"
  */
const roundedAvg = (n, m) => {
  if (n > m) {
    return -1
  } else {
    let avg = (n + m) / 2
    let rounded = Math.round(avg)
    let binary = rounded.toString(2)
    return binary
  }
}
