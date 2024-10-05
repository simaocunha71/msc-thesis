const isEqualToSumEven = (n) => {
  if(n<8 || n%2 !== 0) return false;
  let sum = 0;
  for(let i = 2; i <= n; i += 2){
    sum += i;
    if(sum === n) return true;
  }
  return false;
}
console.log(isEqualToSumEven(4)) // false
console.log(isEqualToSumEven(6)) // false
console.log(isEqualToSumEven(8)) // true
console.log(isEqualToSumEven(10)) // true
console.log(isEqualToSumEven(12)) // true
console.log(isEqualToSumEven(14)) // false
console.log(isEqualToSumEven(16)) // true
console.log(isEqualToSumEven(18)) // false

