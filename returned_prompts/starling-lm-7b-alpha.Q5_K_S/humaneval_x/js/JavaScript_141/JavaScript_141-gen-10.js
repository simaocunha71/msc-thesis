  const validExtensions = ['txt', 'exe', 'dll'];

  const regex = /^[a-zA-Z][a-zA-Z0-9]*\.([a-zA-Z0-9]+)$/;
  if (regex.test(file_name)) {
    const [_, name, extension] = file_name.match(regex);
    if (name.length <= 3 && extension.length == 3 && validExtensions.includes(extension)) {
      return 'Yes';
    }
  }

  return 'No';
}



