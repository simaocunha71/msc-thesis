  const regex = /^[a-zA-Z][a-zA-Z0-9]*\.txt$|^[a-zA-Z][a-zA-Z0-9]*\.exe$|^[a-zA-Z][a-zA-Z0-9]*\.dll$/;
  return regex.test(file_name);
}



