  const regex = /[a-zA-Z][0-9a-zA-Z]*\.[txt|exe|dll]$/g;
  return regex.test(file_name) ? 'Yes' : 'No';
}



