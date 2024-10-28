  if (lst.length == 0) {
    return [];
  }
  var result = [];
  var min = lst[0];
  var max = lst[0];
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < min) {
      min = lst[i];
    }
    if (lst[i] > max) {
      max = lst[i];
    }
  }
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] == min) {
      result.push(max);
      lst.splice(i, 1);
      max = lst[0];
      for (let j = 0; j < lst.length; j++) {
        if (lst[j] > max) {
          max = lst[j];
        }
      }
    }
  }
  for (let i = 0; i < lst.length; i++) {
    result.push(lst[i]);
  }
  return result;
}



