const fileNameCheck = (file_name) => {
  return file_name.match(/^[a-z|A-Z][\w]{0,2}\.(?:txt|exe|dll)$/i)? 'Yes' : 'No';
}

