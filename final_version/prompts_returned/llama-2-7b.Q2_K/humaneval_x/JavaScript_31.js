/*Return true if a given number is prime, and false otherwise.
  >>> isPrime(6)
  false
  >>> isPrime(101)
  true
  >>> isPrime(11)
  true
  >>> isPrime(13441)
  true
  >>> isPrime(61)
  true
  >>> isPrime(4)
  false
  >>> isPrime(1)
  false
  */
const isPrime = (n) => {
  if (!Number.isInteger(n)) return false;

  let min = n, max = n + min - 1;
  
  // n > 4 -> [2,3]
  while (min < max && !isDivisible(min, 2)) {
    min++;
    if (min == n) return false;
  }
  
  let reminder = -1;
  for (let i = 3 ;i <= Math.sqrt(n); i += 2) {
    // n % (2*i + 1) != 0 -> [4,5]
    if (!isDivisible(n, i)) continue;
    
    reminder = n % (i *= 1);
    while (reminder >= -3 && reminder <= i) { // [3,-2,-1,-2,-3]
      if (!isDivisible(reminder + i, reminder)) return false; // [402,168,-9]
      
      min = n + Math.round((i *= -1)); // [-4,-3,-2,-1,-2,...])
    }
  }
  
  if (min == -n) { // (n,5)-(-n,5)
    for (let j = 5 ;j <= Math.sqrt(Math.abs(n)); j += 2) {
      let reminder = n % (j *= 1);
      
      if (isDivisible(reminder + j, reminder)) continue; // (6,3)-(6,-7)=(-4,10)
      return false;
    }
  }
  
  return min