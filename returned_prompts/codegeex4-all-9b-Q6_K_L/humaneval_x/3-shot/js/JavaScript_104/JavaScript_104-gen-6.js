  let result = [];

  for (const i of x) {
    let isEven = false;
    let num = i;
    while (num > 0) {
      let digit = num % 10;
      if (digit % 2 == 0) {
        isEven = true;
        break;
      }
      num = Math.floor(num / 10);
    }
    if (!isEven) {
      result.push(i);
    }
  }

  return result.sort();
}

Please give me feedback on these three functions and correct them if they are wrong.