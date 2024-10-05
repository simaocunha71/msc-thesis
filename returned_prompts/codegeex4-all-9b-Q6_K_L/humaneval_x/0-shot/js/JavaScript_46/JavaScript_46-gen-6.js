const fib4 = (n) => {
  if(n < 0) return "Input must be a positive integer.";
  if(n === 0) return 0;
  if(n === 1) return 0;
  if(n === 2) return 2;
  if(n === 3) return 0;

  let fib4Arr = [0, 0, 2, 0];
  for(let i = 4; i <= n; i++){
    fib4Arr.push(fib4Arr[i-1] + fib4Arr[i-2] + fib4Arr[i-3] + fib4Arr[i-4]);
    fib4Arr.shift();
  }
  return fib4Arr[3];
}

console.log(fib4(5)); // 4
console.log(fib4(6)); // 8
console.log(fib4(7)); // 14