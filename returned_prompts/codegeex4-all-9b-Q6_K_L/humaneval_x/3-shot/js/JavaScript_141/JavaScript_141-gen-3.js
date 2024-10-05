  var digits = 0;
  var dots = 0;
  var letters = 0;

  for (const c of file_name) {
    if (c >= '0' && c <= '9') {
      digits += 1;
    } else if (c == '.') {
      dots += 1;
    } else if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
      letters += 1;
    }
  }

  if (digits > 3 || dots != 1 || letters == 0) {
    return 'No';
  }

  var parts = file_name.split('.');
  if (parts[1] != 'txt' && parts[1] != 'exe' && parts[1] != 'dll') {
    return 'No';
  }

  return 'Yes';
}