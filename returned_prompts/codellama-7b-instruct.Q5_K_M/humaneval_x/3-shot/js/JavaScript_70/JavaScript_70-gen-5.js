  var result = [];
  while (lst.length > 0) {
    var min = lst[0];
    var max = lst[0];
    for (let i = 0; i < lst.length; i++) {
      if (lst[i] < min) {
        min = lst[i];
      } else if (lst[i] > max) {
        max = lst[i];
      }
    }
    result.push(min);
    result.push(max);
    lst = lst.filter(x => x != min && x != max);
  }
  return result;
}



