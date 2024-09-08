  let result = [];
  for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
    let str = i.toString();
    for (let j = 0; j < str.length; j++) {
      if (str[j] % 2 === 0) {
        result.push(Number(str[j]));
      }
    }
  }
  return result;
}



