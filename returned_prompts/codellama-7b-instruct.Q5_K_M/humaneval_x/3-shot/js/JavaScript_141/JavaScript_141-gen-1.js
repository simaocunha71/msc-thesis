  let valid_name = true;
  let valid_extension = false;

  for (let char of file_name) {
    if (char >= '0' && char <= '9') {
      if (valid_name) {
        if (file_name.split('').filter(c => c >= '0' && c <= '9').length > 3) {
          valid_name = false;
        }
      }
    } else if (char == '.') {
      if (valid_name) {
        valid_extension = true;
      }
    } else if (char >= 'a' && char <= 'z') {
      if (!valid_name) {
        valid_name = true;
      }
    } else if (char >= 'A' && char <= 'Z') {
      if (!valid_name) {
        valid_name = true;
      }
    }
  }

  if (valid_name) {
    if (valid_extension) {
      if (file_name.split('.').pop() == 'txt' || file_name.split('.').pop() == 'exe' || file_name.split('.').pop() == 'dll') {
        return 'Yes';
      } else {
        return 'No';
      }
    } else {
      return 'No';
    }
  } else {
    return 'No';
  }
}



