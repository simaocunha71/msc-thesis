  let result = [];
  for (let i = a; i <= b; i++) {
    let str = i.toString();
    for (let j = 0; j < str.length; j++) {
      if (parseInt(str[j]) % 2 === 0) {
        if (!result.includes(i)) {
          result.push(i);
        }
      }
    }
  }
  return result;
}