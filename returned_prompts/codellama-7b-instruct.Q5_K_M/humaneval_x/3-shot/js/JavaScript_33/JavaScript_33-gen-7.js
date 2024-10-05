  var result = [];
  var temp = [];

  for (let i = 0; i < l.length; i++) {
    if (i % 3 == 0) {
      temp.push(l[i]);
    }
  }

  temp.sort();

  for (let i = 0; i < l.length; i++) {
    if (i % 3 == 0) {
      result.push(temp[i]);
    } else {
      result.push(l[i]);
    }
  }

  return result;
}



