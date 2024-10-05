  const regex = /^[A-Za-z][A-Za-z0-9]{0,2}\.(txt|exe|dll)$/;
  return regex.test(file_name) ? 'Yes' : 'No';
}



