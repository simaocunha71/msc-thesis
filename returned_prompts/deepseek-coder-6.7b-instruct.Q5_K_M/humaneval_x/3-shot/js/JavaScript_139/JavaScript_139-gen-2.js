  let result = 1;

  for(let i = n; i > 0; i--) {
    let fact = 1;
    for(let j = 1; j <= i; j++) {
      fact *= j;
    }
    result *= fact;
  }

  return result;
}



