  let result = 1;

  for  (let i = n; i > 0; i--) {
    let fact = 1;
    for  (let j = i; j > 0; j--) {
      fact  *= j;
    }
    result  *= fact;
  }

  return result;
}



