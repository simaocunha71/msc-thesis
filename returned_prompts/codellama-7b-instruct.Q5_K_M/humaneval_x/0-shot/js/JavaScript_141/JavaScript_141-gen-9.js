const fileNameCheck = (file_name) => {
  const str = file_name.split('.');
  if (str.length > 2) {
    return 'No';
  }
  const before = str[0];
  if (before.length === 0 || !before.match(/[A-Za-z]/)) {
    return 'No';
  }
  const after = str[1];
  if (!after.match(/[A-Za-z][A-Za-z]/)) {
    return 'No';
  }
  if (after.length > 3) {
    return 'No';
  }
  return 'Yes';
};
