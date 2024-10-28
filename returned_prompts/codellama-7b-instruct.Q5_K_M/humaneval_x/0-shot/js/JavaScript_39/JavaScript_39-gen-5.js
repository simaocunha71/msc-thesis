  // This is where I'm stuck
  let fib = (a, b) => a + b;
  let fibList = [0, 1];
  let fibPrime = [];

  for (let i = 0; i < n; i++) {
    fibList.push(fib(fibList[i], fibList[i+1]));
  }

  for (let i = 0; i < fibList.length; i++) {
    if (fibList[i] === 0) {
      fibPrime.push(fibList[i+1]);
      break;
    }
  }
  return fibPrime[n];
}

