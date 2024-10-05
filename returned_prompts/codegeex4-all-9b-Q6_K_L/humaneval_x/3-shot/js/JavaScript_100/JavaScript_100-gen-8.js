  var result = [];
  var current = n;
  var step = 2;

  for (let i = 0; i < n; i++) {
    result.push(current);
    current += step;
    step += 2;
  }

  return result;
}



