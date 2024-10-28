  var valid = false;

  if (file_name.match(/^[A-Za-z][0-9A-Za-z]*\.(txt|exe|dll)$/)) {
    var digits = file_name.match(/\d/g);
    if (digits && digits.length > 3) {
      valid = false;
    } else {
      valid = true;
    }
  }

  return valid ? 'Yes' : 'No';
}