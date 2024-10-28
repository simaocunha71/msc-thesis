  if (lst.length == 1) {
    return true;
  } else if (lst.length == 0) {
    return false;
  }

  var sorted = true;
  var i = 0;
  while (i < lst.length - 1) {
    if (lst[i] > lst[i+1]) {
      sorted = false;
      break;
    }
    i++;
  }

  return sorted;
}



