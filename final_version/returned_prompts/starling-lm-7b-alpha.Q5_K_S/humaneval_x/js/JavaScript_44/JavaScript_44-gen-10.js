  let result = [];
  let tmp = x;
  while (tmp > 0) {
    result.push(tmp % base);
    tmp = Math.floor(tmp / base);
  }
  return result.reverse().join('');
}



