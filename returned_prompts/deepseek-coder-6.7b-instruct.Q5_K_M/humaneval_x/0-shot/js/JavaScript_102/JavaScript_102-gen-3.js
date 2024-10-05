  for(let i = y; i >= x; i--){
    if(i % 2 === 0) return i;
  }
  return -1;
}

console.log(chooseNum(12, 15)); // 14
console.log(chooseNum(13, 12)); // -1
console.log(chooseNum(14, 15)); // 14
console.log(chooseNum(15, 16)); // 16
console.log(chooseNum(16, 17)); // 16
console.log(chooseNum(16, 18)); // 16
console.log(chooseNum(17, 18)); // 16
console.log(chooseNum(17, 19)); // 18
console.log(chooseNum(20, 22)); // 20
console.log(chooseNum(23, 24)); // 24
console.log(chooseNum(25, 26)); // 26
console.log(chooseNum(27, 29)); // 28
console.log(chooseNum(30, 30)); // 30
console.log(chooseNum(31, 33)); // 32
console.log(chooseNum(34, 36)); // 34
console.log(chooseNum(37, 39)); // 38
console.log(chooseNum(40, 42)); // 40
console.log(chooseNum(43, 45)); // 44
console.log(chooseNum(46, 48)); // 48
console.log(chooseNum(49, 51)); // 50
console.log(chooseNum(52, 54)); // 52
console.log(chooseNum(55, 57)); // 56
console.log(chooseNum(58, 60)); // 60
console.log(chooseNum(61, 63)); // 62
console.log(chooseNum(64, 66)); //