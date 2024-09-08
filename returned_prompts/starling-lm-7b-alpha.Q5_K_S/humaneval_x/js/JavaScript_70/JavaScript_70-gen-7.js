  let result = [];
  let max_value = Math.max(...lst);
  let min_value = Math.min(...lst);
  let min_index = lst.findIndex(x => x === min_value);
  let max_index = lst.findIndex(x => x === max_value);

  if (min_index < max_index) {
    result = result.concat(min_value, lst.slice(min_index, max_index));
    lst = lst.slice(max_index);
  } else {
    result = result.concat(max_value, lst.slice(max_index, min_index));
    lst = lst.slice(min_index);
  }

  return result.concat(strangeSortList(lst));
}



