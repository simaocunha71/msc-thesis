  const fib4 = (n) => {
    let a = 0;
    let b = 0;
    let c = 2;
    let d = 0;
  
    while (n > 0) {
      if (n % 4 === 0) {
        d = b;
        b = c;
        c = d + c;
        n = Math.floor(n / 4);
      } else if (n % 4 === 1) {
        d = a;
        a = b;
        b = d + b;
        n = Math.floor(n / 4);
      } else if (n % 4 === 2) {
        d = a;
        a = b;
        b = d + b;
        n = Math.floor(n / 4);
      } else {
        d = c;
        c = b;
        b = d + b;
        n = Math.floor(n / 4);
      }
    }
    return a;
  };

  console.log(fib4(5));
  console.log(fib4(6));
  console.log(fib4(7));


