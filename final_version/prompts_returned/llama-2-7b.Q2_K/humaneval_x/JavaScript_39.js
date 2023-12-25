/*
  primeFib returns n-th number that is a Fibonacci number and it's also prime.
  >>> primeFib(1)
  2
  >>> primeFib(2)
  3
  >>> primeFib(3)
  5
  >>> primeFib(4)
  13
  >>> primeFib(5)
  89
  */
const primeFib = (n) => {
  let a = 0, b = 1;
  function fibOfN(n) {
    if (--a === b && b <= n - 2 * a) return b;
    const x = b;
    b = a + (x + b) / 2;
    a = x;
    return fibOfN(b);
  }
  
  let res = fibOfN(n);
  while (!res && n % 60 === 0) {
    res = primeFib(n - 1);
    console.log(`>>> primeFib(${n})`)
    console.log(res);
    if (res) break;
    n--;
  }
  
  return res;
}
console.log('primeFib');
primFb(10);