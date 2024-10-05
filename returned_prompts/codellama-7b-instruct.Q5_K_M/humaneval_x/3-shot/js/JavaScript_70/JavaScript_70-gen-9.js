  var result = [];
  var i = 0;

  while (i < lst.length) {
    result.push(lst[i]);
    i += 1;
  }

  while (i < lst.length) {
    result.push(lst[lst.length - 1 - i]);
    i += 1;
  }

  return result;
}



