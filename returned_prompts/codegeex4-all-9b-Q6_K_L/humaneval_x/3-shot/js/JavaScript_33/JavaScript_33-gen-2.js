  var third = l.filter((val, idx) => idx % 3 == 2);
  third.sort((a, b) => a - b);

  var result = [];
  var third_idx = 0;

  for (let i = 0; i < l.length; i++) {
    if (i % 3 == 2) {
      result.push(third[third_idx]);
      third_idx += 1;
    } else {
      result.push(l[i]);
    }
  }

  return result;
}