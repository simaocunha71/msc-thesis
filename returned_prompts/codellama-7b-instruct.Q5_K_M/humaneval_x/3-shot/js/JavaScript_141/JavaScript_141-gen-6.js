  let max_digit_num = 3;
  let dot_num = 1;
  let letter_num = 1;
  let extension_num = 1;

  if (file_name.length > max_digit_num) {
    return 'No';
  }

  let dot_index = file_name.indexOf('.');
  if (dot_index < 0) {
    return 'No';
  }

  if (dot_index == 0) {
    return 'No';
  }

  let letter_index = file_name.substring(0, dot_index).search(/\w/);
  if (letter_index == -1) {
    return 'No';
  }

  let extension_index = dot_index + 1;
  if (extension_index == file_name.length) {
    return 'No';
  }

  let extension = file_name.substring(extension_index);
  if (extension == 'txt' || extension == 'exe' || extension == 'dll') {
    return 'Yes';
  } else {
    return 'No';
  }
}



