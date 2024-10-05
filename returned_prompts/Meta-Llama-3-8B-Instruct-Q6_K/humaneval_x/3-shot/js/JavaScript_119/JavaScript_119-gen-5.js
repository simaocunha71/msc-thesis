  let open_count = 0;
  let close_count = 0;

  for (let c of lst[0]) {
    if (c == '(') {
      open_count++;
    } else {
      close_count++;
    }
  }

  for (let c of lst[1]) {
    if (c == '(') {
      open_count++;
    } else {
      close_count++;
    }
  }

  if (open_count == close_count) {
    return 'Yes';
  } else {
    return 'No';
  }
}