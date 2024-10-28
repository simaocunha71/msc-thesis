  const validExtensions = ['txt', 'exe', 'dll'];
  const digitsRegex = /\d{4,}/;
  const dotRegex = /\.+/;
  const letterRegex = /^[A-Za-z]/;

  if (digitsRegex.test(file_name)) {
    return 'No';
  }
  if (!dotRegex.test(file_name)) {
    return 'No';
  }
  if (!letterRegex.test(file_name)) {
    return 'No';
  }
  const extension = file_name.split('.').pop();
  if (!validExtensions.includes(extension)) {
    return 'No';
  }
  return 'Yes';
}


