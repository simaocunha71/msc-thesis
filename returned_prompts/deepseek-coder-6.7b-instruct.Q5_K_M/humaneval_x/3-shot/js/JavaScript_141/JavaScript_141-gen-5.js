  const regexp  = /^[a-zA-Z][a-zA-Z0-9]{0,2}\.txt$/;
  const regexp2 = /^[a-zA-Z][a-zA-Z0-9]{0,2}\.exe$/;
  const regexp3 = /^[a-zA-Z][a-zA-Z0-9]{0,2}\.dll$/;
  if  (file_name.match(regexp) || file_name.match(regexp2) || file_name.match(regexp3)) {
    return 'Yes';
  } else {
    return 'No';
  }
}



