  const pattern = /^[a-zA-Z][0-9a-zA-Z]{0,2}\.(?:txt|exe|dll)$/;
  return pattern.test(file_name) ? 'Yes' : 'No';
}



