  var count_open_paren = 0;
  var count_close_paren = 0;

  for (const c of lst[0]) {
    if (c == '(') {
      count_open_paren += 1;
    } else {
      count_close_paren += 1;
    }
  }

  for (const c of lst[1]) {
    if (c == '(') {
      count_open_paren += 1;
    } else {
      count_close_paren += 1;
    }
  }

  if (count_open_paren == count_close_paren) {
    return 'Yes';
  } else {
    return 'No';
  }
}



