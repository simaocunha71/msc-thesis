  var result = [];

  for (const n of numbers) {
    if (numbers.indexOf(n) == numbers.lastIndexOf(n)) {
      result.push(n);
    }
  }

  return result;
}



