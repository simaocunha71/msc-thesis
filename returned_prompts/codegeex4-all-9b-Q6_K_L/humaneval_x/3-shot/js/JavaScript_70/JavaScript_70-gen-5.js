  var result = [];
  var new_lst = lst.slice();

  while (new_lst.length > 0) {
    result.push(Math.min(...new_lst));
    new_lst.splice(new_lst.indexOf(Math.min(...new_lst)), 1);

    if (new_lst.length > 0) {
      result.push(Math.max(...new_lst));
      new_lst.splice(new_lst.indexOf(Math.max(...new_lst)), 1);
    }
  }

  return result;
}



