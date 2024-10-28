  var digits = 0;
  var dot = 0;
  var start = false;
  var valid = false;

  for (const c of file_name) {
    if (c >= '0' && c <= '9') {
      digits += 1;
    } else if (c == '.') {
      dot += 1;
    } else if (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z') {
      start = true;
    } else if (c == '.' && start && valid) {
      break;
    } else {
      return 'No';
    }
  }

  if (digits > 3 || dot != 1 || !start) {
    return 'No';
  }

  var suffix = file_name.split('.')[1];

  if (suffix == 'txt' || suffix == 'exe' || suffix == 'dll') {
    return 'Yes';
  } else {
    return 'No';
  }
}