  let result = [];
  x.forEach(num => {
    if (!(num.toString().split('').some(n => n % 2 == 0))) {
      result.push(num);
    }
  });
  return result.sort((a, b) => a - b);
}



