  let digits = 0;
  let dots = 0;
  let dot_index = 0;
  for (let i = 0; i < file_name.length; i++) {
    if (file_name[i] >= '0' && file_name[i] <= '9') {
      digits += 1;
    } else if (file_name[i] == '.') {
      dots += 1;
      dot_index = i;
    }
  }
  if (dots != 1 || digits > 3 || !(/[a-zA-Z]/.test(file_name[0])) || !['txt', 'exe', 'dll'].includes(file_name.slice(dot_index + 1))) {
    return 'No';
  }
  return 'Yes';
}