  let sum = 0;
  let binary = N.toString(2);
  
  for (let i = 0; i < binary.length; i++) {
    sum += parseInt(binary[i]);
  }
  
  return sum.toString(2);
}

console.log(solve(1000));
console.log(solve(150));
console.log(solve(147));


*/

/*
