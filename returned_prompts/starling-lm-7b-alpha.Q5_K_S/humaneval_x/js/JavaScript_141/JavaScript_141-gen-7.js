  const alphabet = /^[a-zA-Z]+$/;
  const extension = /\.txt$|\.exe$|\.dll$/;

  if (file_name.length > 3) {
    return 'No';
  }
  if (file_name.match(alphabet) === null) {
    return 'No';
  }
  if (file_name.match(extension) === null) {
    return 'No';
  }

  return 'Yes';
}



