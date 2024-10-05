  var result = [];
  var start = 0;
  var end = lst.length - 1;
  while (start <= end) {
    if (start == end) {
      result.push(lst[start]);
    } else {
      result.push(lst[start]);
      result.push(lst[end]);
    }
    start += 1;
    end -= 1;
  }
  return result;
}