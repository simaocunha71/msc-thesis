  let result = l.sort(function(a, b) {
    return a - b;
  });
  let unique_result = [];
  for (let i = 0; i < result.length; i++) {
    if (unique_result.indexOf(result[i]) === -1) {
      unique_result.push(result[i]);
    }
  }
  return unique_result;
}



