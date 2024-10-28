  let result = [];
  for (let i = a; i <= b; i++) {
    let str = i.toString();
    for (let j = 0; j < str.length; j++) {
      if (str[j] % 2 === 0) {
        result.push(parseInt(str[j]));
      }
    }
  }
  return result;
}