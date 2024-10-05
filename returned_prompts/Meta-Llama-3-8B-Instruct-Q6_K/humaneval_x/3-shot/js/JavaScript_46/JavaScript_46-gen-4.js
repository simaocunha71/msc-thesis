  if (n < 1) return 0;
  if (n == 1) return 0;
  if (n == 2) return 2;
  let fib4_0 = 0, fib4_1 = 0, fib4_2 = 2, fib4_3 = 0;
  for (let i = 4; i <= n; i++) {
    let next = fib4_0 + fib4_1 + fib4_2 + fib4_3;
    fib4_0 = fib4_1;
    fib4_1 = fib4_2;
    fib4_2 = fib4_3;
    fib4_3 = next;
  }
  return fib4_3;
}
// or
const fib4 = (n) => {
  if (n < 1) return 0;
  if (n == 1) return 0;
  if (n == 2) return 2;
  let a = 0, b = 0, c = 2, d = 0;
  for (let i = 3; i <= n; i++) {
    let temp = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = temp;
  }
  return d;
}
// or
const fib4 = (n) => {
  if (n < 1) return 0;
  if (n == 1) return 0;
  if (n == 2) return 2;
  let fib4s = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    let next = fib4s[0] + fib4s[1] + fib4s[2] + fib4s[3];
    fib4s.shift();
    fib4s.push(next);
  }
  return fib4s[3];
}