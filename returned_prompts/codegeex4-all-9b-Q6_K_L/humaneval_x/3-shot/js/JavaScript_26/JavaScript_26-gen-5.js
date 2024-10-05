  var result = [];

  for (const number of numbers) {
    if (!result.includes(number)) {
      result.push(number);
    }
  }

  return result;
}



