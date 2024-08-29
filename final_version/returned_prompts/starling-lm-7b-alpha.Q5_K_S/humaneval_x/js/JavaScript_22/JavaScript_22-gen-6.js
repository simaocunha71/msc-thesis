  let result = [];
  for (let v of values) {
    if (typeof v === 'number' && Number.isInteger(v)) {
      result.push(v);
    }
  }
  return result;
}



