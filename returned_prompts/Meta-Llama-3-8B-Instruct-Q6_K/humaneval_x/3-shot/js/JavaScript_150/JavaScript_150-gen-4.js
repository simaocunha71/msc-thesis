  if (isPrime(n)) {
    return x;
  } else {
    return y;
  }
}

const isPrime = (n) => {
  if (n <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}
// Test cases
console.log(xOrY(7, 34, 12)); // 34
console.log(xOrY(15, 8, 5)); // 5
console.log(xOrY(23, 9, 10)); // 9
console.log(xOrY(34, 5, 3)); // 3
console.log(xOrY(37, 25, 30)); // 25
console.log(xOrY(42, 10, 15)); // 15
console.log(xOrY(53, 20, 30)); // 20
console.log(xOrY(55, 15, 10)); // 10
console.log(xOrY(71, 35, 25)); // 35
console.log(xOrY(72, 20, 30)); // 30
console.log(xOrY(101, 40, 50)); // 40
console.log(xOrY(103, 45, 60)); // 45
console.log(xOrY(107, 50, 70)); // 50
console.log(xOrY(111, 55, 80)); // 55
console.log(xOrY(112, 30, 40)); // 40
console.log(xOrY(113, 60, 80)); // 60
console.log(xOrY(114, 40, 50)); // 50
console.log(xOrY(115, 70, 90)); // 70
console.log(xOrY(116, 50, 60)); // 60
console.log(xOrY(117, 80, 100)); // 80
console.log(xOrY(118, 60, 70)); // 70
console.log(xOrY(119, 90, 110)); // 90
console.log(xOrY(120, 70, 80)); // 80
console.log(xOrY