  let fib4_array = [0, 0, 2, 0];
  if (n < 4) {
    return fib4_array[n];
  }

  for (let i = 4; i <= n; i++) {
    let fib = fib4_array[0] + fib4_array[1] + fib4_array[2] + fib4_array[3];
    fib4_array.shift();
    fib4_array.push(fib);
  }

  return fib4_array[3];
}