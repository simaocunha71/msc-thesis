  const regex = /^[a-zA-Z]\w+\.(txt|exe|dll)$/;
  if (regex.test(file_name)) {
    return 'Yes';
  } else {
    return 'No';
  }
}



