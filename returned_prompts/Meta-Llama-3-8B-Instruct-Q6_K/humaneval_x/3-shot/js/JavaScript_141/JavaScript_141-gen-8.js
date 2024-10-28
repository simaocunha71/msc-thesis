  let valid = true;
  let dot_index = file_name.indexOf('.');
  let extension = file_name.substring(dot_index + 1);
  let name = file_name.substring(0, dot_index);

  if (name.match(/\d{4,}/) || extension.match(/\d{4,}/)) {
    valid = false;
  }

  if (!name.match(/^[a-zA-Z]/) || extension !== 'txt' && extension !== 'exe' && extension !== 'dll' || dot_index === -1 || name === '') {
    valid = false;
  }

  return valid ? 'Yes' : 'No';
}