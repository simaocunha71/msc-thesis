  var name_parts = file_name.split('.');
  var name = name_parts[0];
  var extension = name_parts[1];
  var name_digits = name.match(/\d/g);
  var name_letters = name.match(/[a-zA-Z]/g);

  if (name_digits.length > 3) {
    return 'No';
  } else if (name_parts.length != 2) {
    return 'No';
  } else if (name_letters === null) {
    return 'No';
  } else if (extension != 'txt' && extension != 'exe' && extension != 'dll') {
    return 'No';
  } else {
    return 'Yes';
  }
}



