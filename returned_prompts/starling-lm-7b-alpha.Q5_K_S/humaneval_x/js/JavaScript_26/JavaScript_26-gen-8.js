  let seen = {};
  let result = [];

  for (const number of numbers) {
    if (!(number in seen)) {
      seen[number] = true;
      result.push(number);
    }
  }

  return result;
}



