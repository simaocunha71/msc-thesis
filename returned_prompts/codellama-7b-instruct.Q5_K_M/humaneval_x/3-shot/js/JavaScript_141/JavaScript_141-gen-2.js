  const regex = /^[a-zA-Z][a-zA-Z0-9]{0,2}\.(txt|exe|dll)$/;
  return regex.test(file_name) ? 'Yes' : 'No';
}



