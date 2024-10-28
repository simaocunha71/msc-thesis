  const match = /^[a-zA-Z]\.[a-zA-Z0-9]{0,3}$/.exec(file_name);
  if (match != null) {
    if (match[1] == 'exe' || match[1] == 'dll' || match[1] == 'txt') {
      return 'Yes';
    }
    else {
      return 'No';
    }
  }
  else {
    return 'No';
  }
}



