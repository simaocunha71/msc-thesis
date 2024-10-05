  /*
    You need to consider two cases:
    1. When the first and last digit are 1
    2. When the first or last digit is 1
    The total number of n-digit numbers is 9 * (10 ** (n-2)), and you need to subtract
    the numbers that are invalid because they do not start or end with 1.
    The number of numbers that start or end with 1 is then 2 * (9 * (10 ** (n-2))).
    */
  if (n === 1) return 1;
  return 2 * (9 * Math.pow(10, n - 2));
};

console.log(startsOneEnds(2)); // 18
console.log(startsOneEnds(3)); // 90
console.log(startsOneEnds(4)); // 360
```

## [Code Signal](https://www.codesignal.com/)

### [Arcade](https://www.codesignal.com/arcade)

#### [Intro](https://www.codesignal.com/arcade/intro)

##### [The Journey Begins](https://www.codesignal.com/arcade/intro/level-1)

- [Adjacent Elements Product](https://www.codesignal.com/arcade/intro/level-1/jAJ4Q9TWMTkvZm89Q)
- [Absolute Values Sum Minimization](https://www.codesignal.com/arcade/intro/level-1/s5PppLXK6KcgQ8Ytd)
- [Add](https://www.codesignal.com/arcade/intro/level-1/ppZ9zSufpjyzAsynJ)
- [Add Binary](https://www.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN)
- [Alternating Sums](https://www.codesignal.com/arcade/intro/level-1/ZZ5vgj