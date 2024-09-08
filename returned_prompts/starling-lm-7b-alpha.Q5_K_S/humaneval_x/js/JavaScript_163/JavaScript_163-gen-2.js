  let result = [];
  for (let i = a; i <= b; i++) {
    let s = i.toString();
    for (let c of s) {
      if (c % 2 == 0) {
        result.push(c);
      }
    }
  }
  result.sort((a, b) => a - b);
  return result;
}



