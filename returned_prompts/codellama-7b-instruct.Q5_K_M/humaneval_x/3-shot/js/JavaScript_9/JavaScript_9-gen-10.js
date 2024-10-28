  var result = [];
  for (let i = 0; i < numbers.length; i++) {
    result.push(Math.max(...numbers.slice(0, i + 1)));
  }
  return result;
}



