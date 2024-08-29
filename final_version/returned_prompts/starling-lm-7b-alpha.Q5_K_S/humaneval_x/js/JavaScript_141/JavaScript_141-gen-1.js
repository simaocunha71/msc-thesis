  let result = 'Yes';
  let count = 0;
  let letter = true;
  let substring = file_name.split('.')[1];

  if (file_name.split('.').length != 2) {
    result = 'No';
  } else {
    for (const c of file_name) {
      if (c == '.') {
        count += 1;
      } else if (c >= '0' && c <= '9') {
        count += 1;
      } else if (c >= 'a' && c <= 'z') {
        letter = false;
      } else if (c >= 'A' && c <= 'Z') {
        letter = false;
      }
    }
    if (count > 3) {
      result = 'No';
    } else if (!letter) {
      result = 'No';
    } else if (substring != 'txt' && substring != 'exe' && substring != 'dll') {
      result = 'No';
    }
  }

  return result;
}



