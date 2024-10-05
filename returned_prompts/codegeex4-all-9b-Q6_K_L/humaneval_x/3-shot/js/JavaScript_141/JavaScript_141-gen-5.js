  var valid_extensions = ['txt', 'exe', 'dll'];
  var valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  var digits = '0123456789';
  var dot_count = 0;
  var digit_count = 0;
  var before_dot = '';
  var after_dot = '';

  for (var i = 0; i < file_name.length; i++) {
    if (digits.includes(file_name[i])) {
      digit_count += 1;
    } else if (file_name[i] == '.') {
      dot_count += 1;
    } else if (valid_chars.includes(file_name[i])) {
      before_dot += file_name[i];
    } else {
      return 'No';
    }
  }

  if (dot_count == 1 && digit_count <= 3) {
    after_dot = file_name.split('.')[1];
  }

  if (valid_extensions.includes(after_dot)) {
    return 'Yes';
  } else {
    return 'No';
  }
}