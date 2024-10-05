  var result = [];
  for (const n of numbers) {
    result.push(n);
    result.push(delimeter);
  }
  return result.slice(0, -1);
}



