  const result = [];
  let a = 0;
  let b = 0;
  let c = 3;
  while (result.length < n + 1) {
    result.push(c);
    let tmp = a;
    a = b;
    b = c;
    c = tmp + b + c;
  }
  return result;
}



