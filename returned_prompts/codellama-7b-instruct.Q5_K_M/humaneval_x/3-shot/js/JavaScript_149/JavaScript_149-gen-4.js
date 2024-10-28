  var sorted_lst = lst.sort(function(a, b){return a.length - b.length});
  var result = [];
  for (var i = 0; i < sorted_lst.length; i++) {
    if (sorted_lst[i].length % 2 == 0) {
      result.push(sorted_lst[i]);
    }
  }

  return result;
}



