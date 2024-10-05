  if (lst.length == 0) {
    return [];
  }

  let result = [lst[0]];
  let min = lst[0];
  let max = lst[0];
  for (let i = 1; i < lst.length; i++) {
    if (lst[i] < min) {
      min = lst[i];
    }
    if (lst[i] > max) {
      max = lst[i];
    }
  }

  if (min != lst[0]) {
    result.push(max);
  }

  if (lst.length > 1) {
    if (lst[1] != min && lst[1] != max) {
      result.push(min);
    }
    result = result.concat(strangeSortList(lst.slice(1, lst.length - 1)));
    if (lst[lst.length - 1] != min && lst[lst.length - 1] != max) {
      result.push(max);
    }
  }

  return result;
}



