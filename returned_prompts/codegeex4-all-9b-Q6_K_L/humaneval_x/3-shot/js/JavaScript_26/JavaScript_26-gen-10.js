  var result = [];

  for (const number of numbers) {
    if (result.indexOf(number) == -1) {
      result.push(number);
    }
  }

  return result;
}



