  let result = [];
  for (const value of values) {
    if (typeof value === 'number' && Math.floor(value) === value) {
      result.push(value);
    }
  }
  return result;
}



