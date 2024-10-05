    if (b == 0) {
        return a;
    }
    else {
        return greatestCommonDivisor(b, a % b);
    }
}


/*
  >>> isEven(2)
  True
  >>> isEven(3)
  False
  */
const isEven = (number) => {
    return number % 2 === 0;
}


/*
  >>> factorize(28)
  [2, 2, 7]
  >>> factorize(20)
  [2, 2, 5]
  >>> factorize(10)
  [2, 5]
  >>> factorize(9)
  [3, 3]
  >>> factorize(81)
  [3, 3, 7]
  */
const factorize = (n) => {
    let factors = [];
    for (let i = 2; i <= n; i++) {
        while (n % i === 0) {
            factors.push(i);
            n /= i;
        }
    }
    return factors;
}


/*
  >>> removeVowels('hello')
  'hll'
  >>> removeVowels('python')
  'pythn'
  >>> removeVowels('elephant')
  'lphnt'
  */
const removeVowels = (s) => {
    const vowels = 'aeiouAEIOU';
    return s.split('').filter(c => !vowels.includes(c)).join('');
}


/*
  >>> isPrime(2)
  True
  >>> isPrime(3)
  True
  >>> isPrime(4)
  False
  >>> isPrime(5)
  True
  >>> isPrime(6)
  False
  >>> isPrime(7)
  True
  >>> isPrime(8)
  False
  >>> isPrime(10)
  False
  >>> isPrime(11)
  True
  >>> isPrime(12)
  False
  >>> isPrime(1