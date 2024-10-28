  let count = 0;
  for (let i = 11; i < n; i += 11) {
    if (String(i).includes(7)) {
      count++;
    }
  }
  for (let i = 13; i < n; i += 13) {
    if (String(i).includes(7)) {
      count++;
    }
  }
  return count;
};

fizzBuzz(79);

/*
Return an array of all prime numbers less than n.
  >>> sieve(10)
  [2, 3, 5, 7]
  >>> sieve(15)
  [2, 3, 5, 7, 11, 13]
  >>> sieve(20)
  [2, 3, 5, 7, 11, 13, 17, 19]

  */
const sieve = n => {
  const arr = Array.from({ length: n }, (_, i) => i + 1);
  const limit = Math.floor(Math.sqrt(n));

  for (let i = 2; i <= limit; i++) {
    if (arr[i] === i) {
      for (let j = i * i; j < n; j += i) {
        arr[j] = 0;
      }
    }
  }

  return arr.filter(val => val);
};

sieve(20);




















































































































































