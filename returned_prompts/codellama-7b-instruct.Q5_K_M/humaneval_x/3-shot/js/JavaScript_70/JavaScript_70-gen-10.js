  var result = [];

  var min = lst[0];
  var max = lst[0];

  for (let i = 1; i < lst.length; i++) {
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
    } else if (lst[i] == max) {
      result.push(min);
    } else {
      result.push(lst[i]);
    }
  }

  return result;
}



