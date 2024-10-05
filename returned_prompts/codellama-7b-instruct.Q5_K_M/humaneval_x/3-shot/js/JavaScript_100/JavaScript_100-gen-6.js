  if (n < 0) {
    return null;
  }

  var result = [];
  var next_level = n;

  for (let i = 0; i < n; i++) {
    result.push(next_level);
    next_level = (next_level % 2 == 0) ? next_level + 1 : next_level + 2;
  }

  return result;
}



