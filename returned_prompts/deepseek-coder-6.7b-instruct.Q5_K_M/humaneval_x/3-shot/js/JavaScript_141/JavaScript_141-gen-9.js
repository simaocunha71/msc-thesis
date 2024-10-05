  const valid_extensions = ["txt", "exe", "dll"];
  const digit_count = (file_name.match(/\d/g) || []).length;
  const dot_count = (file_name.match(/\./g) || []).length;
  const extension = file_name.split('.').pop();
  const first_char = file_name.charAt(0);

  if (digit_count > 3 || dot_count != 1 || !valid_extensions.includes(extension) ||
      !(first_char.match(/[a-zA-Z]/g)) ) {
    return "No";
  }
  return "Yes";
}



