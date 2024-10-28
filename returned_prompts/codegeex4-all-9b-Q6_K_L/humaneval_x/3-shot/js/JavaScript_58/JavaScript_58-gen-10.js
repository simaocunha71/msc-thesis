  var result = [];

  for (var i = 0; i < l1.length; i++) {
    if (l2.includes(l1[i]) && !result.includes(l1[i])) {
      result.push(l1[i]);
    }
  }

  return result.sort((a, b) => a - b);
}



