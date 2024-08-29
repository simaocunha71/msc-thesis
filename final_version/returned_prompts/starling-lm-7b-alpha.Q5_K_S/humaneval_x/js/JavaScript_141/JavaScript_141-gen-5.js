  const latinAlphabet = /^[a-zA-Z]+$/;
  const fileExtension = /^(txt|exe|dll)$/;
  const regex = new RegExp(`^${latinAlphabet}.*\\.${fileExtension}$`);

  if (regex.test(file_name)) {
    return 'Yes';
  } else {
    return 'No';
  }
}



