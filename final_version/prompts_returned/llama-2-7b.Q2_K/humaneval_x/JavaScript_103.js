/*You are given two positive integers n and m, and your task is to compute the
  average of the integers from n through m (including n and m). 
  Round the answer to the nearest integer and convert that to binary.
  If n is greater than m, return -1.
  Example:
  roundedAvg(1, 5) => "0b11"
  roundedAvg(7, 5) => -1
  roundedAvg(10, 20) => "0b1111"
  roundedAvg(20, 33) => "0b11010"
  */
const roundedAvg = (n, m) => {
    let a = n;
    let b = m;
     if(a > b){return -1};
    const averageNumber = (n + m ) / 2;
    console.log(averageNumber);
    return averageNumber;
}