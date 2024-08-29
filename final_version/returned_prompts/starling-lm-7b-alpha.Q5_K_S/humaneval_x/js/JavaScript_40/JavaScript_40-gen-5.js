  const len = l.length;
  for (var i = 0; i < len; i++) {
    for (var j = i + 1; j < len; j++) {
      for (var k = j + 1; k < len; k++) {
        if (l[i] + l[j] + l[k] === 0) {
          return true;
        }
      }
    }
  }
  return false;
}



