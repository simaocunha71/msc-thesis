  var result = [];

  for (let i = 0; i < lst.length; i++) {
    if (i == 0) {
      result.push(lst[0]);
    } else {
      if (i == lst.length - 1) {
        result.push(lst[i]);
        result.push(lst[0]);
      } else {
        if (i % 2 == 0) {
          result.push(lst[lst.length - i - 1]);
          result.push(lst[i]);
        } else {
          result.push(lst[i]);
          result.push(lst[lst.length - i - 1]);
        }
      }
    }
  }

  return result;
}



