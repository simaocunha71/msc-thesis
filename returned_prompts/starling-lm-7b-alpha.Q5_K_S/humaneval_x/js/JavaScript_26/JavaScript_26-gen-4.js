  let result = [];

  for (const n of numbers) {
    if (result.indexOf(n) === -1) {
      result.push(n);
    }
  }

  return result;
}



