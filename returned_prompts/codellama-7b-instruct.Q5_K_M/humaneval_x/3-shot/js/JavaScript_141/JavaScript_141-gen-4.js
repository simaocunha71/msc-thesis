  const valid_name_pattern = /^[a-zA-Z]\w*[.][txt|exe|dll]$/;
  const valid_name_regex = new RegExp(valid_name_pattern);

  if (valid_name_regex.test(file_name)) {
    return 'Yes';
  } else {
    return 'No';
  }
}



