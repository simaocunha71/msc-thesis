  let result = [];
  let number = x;
  while (number > 0) {
    result.push(number % base);
    number = Math.floor(number / base);
  }
  return result.reverse().join('');
}



