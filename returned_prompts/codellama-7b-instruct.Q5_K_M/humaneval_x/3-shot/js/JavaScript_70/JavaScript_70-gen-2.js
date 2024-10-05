  if (lst.length == 0) {
    return [];
  }

  var result = [lst[0]];
  lst.splice(0, 1);

  for (var i = 0; i < lst.length; i++) {
    result.push(lst[i]);
    lst.splice(i, 1);
  }

  result.push(lst[0]);
  return result;
}



