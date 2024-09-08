  let result = [];
  for (let i = 0; i < x.length; i++) {
    let str = x[i].toString();
    let isEven = false;
    for (let j = 0; j < str.length; j++) {
      if (parseInt(str[j]) % 2 == 0) {
        isEven = true;
        break;
      }
    }
    if (!isEven) {
      result.push(x[i]);
    }
  }
  return result.sort((a, b) => a - b);
}



