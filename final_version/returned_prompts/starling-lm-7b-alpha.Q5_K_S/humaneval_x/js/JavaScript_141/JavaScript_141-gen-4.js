  const latin_alpha_regex = /^[a-zA-Z]$/;
  const extensions = ['txt', 'exe', 'dll'];
  const dot_index = file_name.indexOf('.');
  const first_char_index = file_name.indexOf(file_name[dot_index - 1]);

  if (dot_index === -1) {
    return 'No';
  }
  if (first_char_index === -1 || !latin_alpha_regex.test(file_name[dot_index - 1])) {
    return 'No';
  }
  const ext = file_name.slice(dot_index + 1).toLowerCase();
  if (!extensions.includes(ext)) {
    return 'No';
  }
  const digits_count = (file_name + 'a').split(/[0-9]/).length - 1;
  if (digits_count > 3) {
    return 'No';
  }

  return 'Yes';
}



