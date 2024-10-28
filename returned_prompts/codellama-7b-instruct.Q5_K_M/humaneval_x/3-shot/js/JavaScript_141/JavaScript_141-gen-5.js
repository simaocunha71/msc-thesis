  if (file_name.length <= 3 && file_name.includes('.') && file_name[0] != '.') {
    const name_before_dot = file_name.split('.')[0];
    const name_after_dot = file_name.split('.')[1];
    if (name_before_dot.length > 0 && (name_after_dot == 'txt' || name_after_dot == 'exe' || name_after_dot == 'dll')) {
      return 'Yes';
    }
  }
  return 'No';
}



