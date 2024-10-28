const fib4 = (n) => {
  let a = 0;
  let b = 0;
  let c = 2;
  if (n === 0) return a;
  if (n === 1) return b;
  if (n === 2) return c;
  if (n === 3) return a + b + c;
  if (n === 4) return a + b;
  if (n === 5) return b + c;
  if (n === 6) return a + b + c + b + a;
  if (n === 7) return a + b + c + b + a + c;
  if (n === 8) return a + b + c + b + a + c + a + b;
  if (n === 9) return a + b + c + b + a + c + a + b + c;
  if (n === 10) return a + b + c + b + a + c + a + b + c + a + b;

